---
description: Repository Information Overview
alwaysApply: true
---

# File Management System Information

## Summary

A fullstack file management application built with **Django 4.2.7**, vanilla JavaScript, and SQLite3. Enables users to upload, search, filter, and export files with a responsive web interface. Supports file type detection, Excel export, pagination, and download/delete operations. Configured for Heroku deployment with gunicorn and WhiteNoise.

## Structure

```
file management system/
├── config/                  # Django project settings
│   ├── settings.py         # Main configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py
├── records/                # Main Django application
│   ├── migrations/         # Database migrations
│   ├── static/
│   │   ├── css/style.css   # Responsive styling
│   │   └── js/script.js    # Client-side interactivity
│   ├── templates/
│   │   └── records/list.html  # Main UI template
│   ├── models.py           # FileRecord model
│   ├── views.py            # View logic (upload, search, filter, export)
│   ├── urls.py             # App URL routing
│   ├── forms.py            # Upload form validation
│   └── admin.py
├── media/                  # Uploaded files directory
├── manage.py               # Django CLI
├── requirements.txt        # Python dependencies
├── Procfile                # Heroku deployment config
├── SETUP.md                # Detailed setup guide
└── README.md               # Full documentation
```

## Language & Runtime

**Language**: Python  
**Version**: 3.8+  
**Build System**: Django (Framework)  
**Package Manager**: pip  
**Framework**: Django 4.2.7  
**Frontend**: HTML5, CSS3, Vanilla JavaScript

## Dependencies

**Main Dependencies**:
- **Django 4.2.7** - Web framework
- **xlsxwriter 3.1.9** - Excel file generation
- **python-dateutil 2.8.2** - Date utilities
- **Pillow 12.0.0** - Image handling
- **gunicorn** - WSGI HTTP server (production)
- **whitenoise** - Static file serving

**Development**: All dependencies use pip for installation.

## Build & Installation

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Mac/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Access**: http://localhost:8000

## Docker

**Procfile** (Heroku deployment):
```
web: python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

**Configuration**: 
- Uses WhiteNoise middleware for static file serving
- Gunicorn for production WSGI server
- Supports environment variable `DEBUG` (default: 'True')
- Database: SQLite3 (file-based, can switch to PostgreSQL)
- Max file upload: 10 MB

## Main Files & Resources

**Entry Points**:
- `manage.py` - Django management CLI
- `config/wsgi.py` - WSGI application entry point

**Configuration**:
- `config/settings.py` - Django settings, database, static/media paths
- `records/models.py` - FileRecord model with auto file-type detection

**Key Endpoints**:
- `/` - List, search, filter records with pagination
- `/upload/` - Upload new file
- `/download/<id>/` - Download file
- `/delete/<id>/` - Delete record
- `/export/` - Export filtered results to Excel

**Application Structure**:
- Single Django app (`records/`) with file management functionality
- Database model stores: description, file, upload_datetime, file_type, file_date, letter_reference_number
- File types auto-detected: PDF, DOCX, XLSX, Image, Other
- Pagination: 10 records per page
- SQLite database: `db.sqlite3`

## Database

**Engine**: Django ORM with SQLite3 backend  
**Model**: FileRecord
- `id` - Primary key
- `description` - Text field (required)
- `file` - FileField with auto upload_to='uploads/'
- `upload_datetime` - DateTime (auto-set)
- `file_type` - Auto-detected from file extension
- `file_date` - Optional date field
- `letter_reference_number` - Optional reference number

**Features**:
- Auto file-type detection based on extension
- Ordered by newest upload first
- Default ordering: `-upload_datetime`

## Testing & Validation

**Test File**: `test_imports.py` (basic import validation)  
**Framework**: Django's built-in test command  
**Validation Approach**:
- Server-side file upload validation
- File type verification via extension
- File size limits (10 MB max)
- CSRF protection enabled
- SQL injection protection via Django ORM

**Test Command**:
```bash
python manage.py test
```

## Security

- CSRF middleware enabled
- Server-side file upload validation
- File size limits enforced (10 MB)
- File type verification
- SQL injection protection via Django ORM
- Django password validators configured
- Static files compression via WhiteNoise
- Secure file storage outside web root (`/media/`)

## Deployment Notes

**Production Requirements** (before deployment):
1. Change `SECRET_KEY` in `config/settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Migrate to PostgreSQL instead of SQLite for production
5. Set up proper static/media file serving (nginx, etc.)
6. Enable HTTPS
7. Use environment variables for sensitive data
