from django.contrib import admin
from .models import FileRecord


@admin.register(FileRecord)
class FileRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'file_type', 'upload_datetime']
    list_filter = ['file_type', 'upload_datetime']
    search_fields = ['description']
    readonly_fields = ['upload_datetime', 'file_type']
