import os
import zipfile
from io import BytesIO
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import FileResponse, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from datetime import datetime
import xlsxwriter

from .models import FileRecord
from .forms import FileRecordForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('list_records')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('list_records')
        else:
            return render(request, 'records/login.html', {'error': 'Invalid credentials. Please try again.'})
    
    return render(request, 'records/login.html')


@login_required(login_url='login')
def list_records(request):
    """List, search, and filter records with pagination. Also handles file uploads."""
    
    upload_form = FileRecordForm()
    
    if request.method == 'POST':
        upload_form = FileRecordForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('list_records')
        else:
            for field, errors in upload_form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    
    records = FileRecord.objects.all()
    search_query = request.GET.get('search', '').strip()
    file_type = request.GET.get('file_type', '').strip()
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    sort_by = request.GET.get('sort_by', '-upload_datetime').strip()
    
    if search_query:
        records = records.filter(Q(description__icontains=search_query))
    
    if file_type and file_type != 'All':
        records = records.filter(file_type=file_type)
    
    if start_date:
        try:
            start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
            records = records.filter(upload_datetime__date__gte=start_datetime.date())
        except ValueError:
            pass
    
    if end_date:
        try:
            end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
            records = records.filter(upload_datetime__date__lte=end_datetime.date())
        except ValueError:
            pass
    
    if sort_by == 'upload_date_asc':
        records = records.order_by('upload_datetime')
    elif sort_by == 'upload_date_desc':
        records = records.order_by('-upload_datetime')
    elif sort_by == 'description_asc':
        records = records.order_by('description')
    elif sort_by == 'description_desc':
        records = records.order_by('-description')
    else:
        records = records.order_by('-upload_datetime')
    
    file_types = FileRecord.FILE_TYPE_CHOICES
    
    paginator = Paginator(records, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'upload_form': upload_form,
        'search_query': search_query,
        'file_type': file_type,
        'start_date': start_date,
        'end_date': end_date,
        'sort_by': sort_by,
        'file_types': file_types,
        'total_records': records.count(),
    }
    
    return render(request, 'records/list.html', context)


@login_required(login_url='login')
def upload_record(request):
    """Handle file upload"""
    
    if request.method == 'POST':
        form = FileRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('list_records')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = FileRecordForm()
    
    return redirect('list_records')


@login_required(login_url='login')
def edit_record(request, record_id):
    """Edit a record's metadata"""
    
    record = get_object_or_404(FileRecord, id=record_id)
    
    if request.method == 'POST':
        form = FileRecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully!')
            return redirect('list_records')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = FileRecordForm(instance=record)
    
    context = {
        'form': form,
        'record': record,
    }
    
    return render(request, 'records/edit.html', context)


@login_required(login_url='login')
def download_file(request, record_id):
    """Download a file"""
    
    record = get_object_or_404(FileRecord, id=record_id)
    
    if record.file:
        file_path = record.file.path
        if os.path.exists(file_path):
            return FileResponse(
                open(file_path, 'rb'),
                as_attachment=True,
                filename=record.file_name
            )
    
    messages.error(request, 'File not found.')
    return redirect('list_records')


@login_required(login_url='login')
@require_POST
def delete_record(request, record_id):
    """Delete a record and its file"""
    
    record = get_object_or_404(FileRecord, id=record_id)
    
    if record.file:
        try:
            if os.path.exists(record.file.path):
                os.remove(record.file.path)
        except Exception as e:
            messages.error(request, f'Error deleting file: {str(e)}')
    
    record.delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('list_records')


@login_required(login_url='login')
def export_to_excel(request):
    """Export filtered records to Excel with logo header and embedded files in ZIP"""
    
    records = FileRecord.objects.all()
    search_query = request.GET.get('search', '').strip()
    file_type = request.GET.get('file_type', '').strip()
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()
    sort_by = request.GET.get('sort_by', '-upload_datetime').strip()
    
    if search_query:
        records = records.filter(Q(description__icontains=search_query))
    
    if file_type and file_type != 'All':
        records = records.filter(file_type=file_type)
    
    if start_date:
        try:
            start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
            records = records.filter(upload_datetime__date__gte=start_datetime.date())
        except ValueError:
            pass
    
    if end_date:
        try:
            end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
            records = records.filter(upload_datetime__date__lte=end_datetime.date())
        except ValueError:
            pass
    
    if sort_by == 'upload_date_asc':
        records = records.order_by('upload_datetime')
    elif sort_by == 'upload_date_desc':
        records = records.order_by('-upload_datetime')
    elif sort_by == 'description_asc':
        records = records.order_by('description')
    elif sort_by == 'description_desc':
        records = records.order_by('-description')
    else:
        records = records.order_by('-upload_datetime')
    
    excel_buffer = BytesIO()
    workbook = xlsxwriter.Workbook(excel_buffer)
    worksheet = workbook.add_worksheet('File Records')
    
    logo_path = os.path.join(settings.BASE_DIR, 'records', 'static', 'images', 'logo.png')
    if os.path.exists(logo_path):
        try:
            worksheet.set_header('&C&G', {'image_center': logo_path})
        except Exception:
            pass
    
    header_row = 4
    headers = ['Serial Number', 'Description', 'File Date', 'Letter Reference', 'File Name', 'File Type', 'Upload Date & Time']
    
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#4472C4',
        'font_color': 'white',
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    
    for col, header in enumerate(headers):
        worksheet.write(header_row, col, header, header_format)
    
    cell_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    
    text_format = workbook.add_format({
        'align': 'left',
        'valign': 'vcenter',
        'border': 1
    })
    
    date_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1,
        'num_format': 'yyyy-mm-dd'
    })
    
    worksheet.set_column('A:A', 12)
    worksheet.set_column('B:B', 25)
    worksheet.set_column('C:C', 12)
    worksheet.set_column('D:D', 18)
    worksheet.set_column('E:E', 25)
    worksheet.set_column('F:F', 12)
    worksheet.set_column('G:G', 20)
    
    row_num = header_row + 1
    for record in records:
        worksheet.write(row_num, 0, record.id, cell_format)
        worksheet.write(row_num, 1, record.description, text_format)
        
        if record.file_date:
            worksheet.write_datetime(row_num, 2, record.file_date, date_format)
        else:
            worksheet.write(row_num, 2, '', cell_format)
        
        worksheet.write(row_num, 3, record.letter_reference_number or '', cell_format)
        worksheet.write(row_num, 4, record.file_name, text_format)
        worksheet.write(row_num, 5, record.file_type, cell_format)
        worksheet.write(row_num, 6, record.upload_datetime.strftime('%Y-%m-%d %H:%M:%S'), cell_format)
        
        row_num += 1
    
    workbook.close()
    excel_buffer.seek(0)
    
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr('records.xlsx', excel_buffer.getvalue())
        
        for i, record in enumerate(records, 1):
            file_path = os.path.join(settings.MEDIA_ROOT, record.file.name)
            if os.path.exists(file_path):
                try:
                    file_name = record.file_name
                    name_without_ext = os.path.splitext(file_name)[0]
                    ext = os.path.splitext(file_name)[1]
                    unique_filename = f"{i:03d}_{name_without_ext}{ext}"
                    
                    zip_file.write(file_path, arcname=f"files/{unique_filename}")
                except Exception:
                    pass
    
    zip_buffer.seek(0)
    
    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="file_records_export.zip"'
    
    return response
