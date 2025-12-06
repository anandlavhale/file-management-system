# File Reference Guide

Complete documentation of every file in the File Management System project.

## Root Level Files

### `manage.py`
- **Purpose**: Django command-line utility for administrative tasks
- **Usage**: Run all Django commands (runserver, makemigrations, migrate, etc.)
- **Don't modify**: Unless you know what you're doing

### `requirements.txt`
- **Purpose**: Lists all Python package dependencies with versions
- **Content**:
  - Django==4.2.7 (Web framework)
  - openpyxl==3.11.0 (Excel generation)
  - python-dateutil==2.8.2 (Date utilities)
- **Usage**: `pip install -r requirements.txt`

### `README.md`
- **Purpose**: Main project documentation and getting started guide
- **Content**: Features, quick start, tech stack, usage guide, FAQ

### `SETUP.md`
- **Purpose**: Comprehensive setup and deployment guide
- **Content**: Detailed installation steps, troubleshooting, configuration options, project structure explanation

### `QUICKSTART.txt`
- **Purpose**: Fast setup guide for experienced developers
- **Content**: Minimal setup steps for Windows and Mac/Linux

### `FILE_REFERENCE.md`
- **Purpose**: This file - documents every file in the project
- **Content**: File descriptions and purposes

### `.gitignore`
- **Purpose**: Specifies files/folders to ignore in Git version control
- **Content**: Python cache, virtual environments, database, media files, IDE configs

---

## `config/` Directory

Django project configuration files.

### `config/__init__.py`
- **Purpose**: Makes the config directory a Python package
- **Content**: Empty (required by Python)

### `config/settings.py`
- **Purpose**: Main Django configuration file
- **Key Settings**:
  - `INSTALLED_APPS`: Registered Django apps (admin, auth, records)
  - `DATABASES`: SQLite3 database configuration
  - `TEMPLATES`: HTML template configuration
  - `MEDIA_ROOT/MEDIA_URL`: File upload configuration
  - `STATIC_ROOT/STATIC_URL`: Static files configuration
- **Modify**: When adding new apps, changing database, or customizing settings

### `config/urls.py`
- **Purpose**: Main URL router - maps URLs to app-specific URLs
- **Content**:
  - `/admin/`: Django admin panel
  - `/`: Points to records app URLs
  - Media and static file serving (development only)
- **Modify**: When adding new apps or URL patterns

### `config/wsgi.py`
- **Purpose**: WSGI application entry point for production servers
- **Don't modify**: Unless deploying to production

---

## `records/` Directory

Main Django application - contains all business logic, models, forms, views, and templates.

### `records/__init__.py`
- **Purpose**: Makes records directory a Python package
- **Content**: Empty (required by Python)

### `records/models.py`
- **Purpose**: Database models definition
- **Key Model: FileRecord**
  - `id`: Auto-increment primary key
  - `description`: Text field for file description
  - `file`: FileField for storing uploaded files
  - `upload_datetime`: Auto-set timestamp
  - `file_type`: Auto-detected file type (PDF, DOCX, XLSX, Image, Other)
- **Methods**:
  - `save()`: Auto-detects file type on save
  - `file_name` property: Returns filename without path
- **Modify**: To add new fields, change file types, or customize model behavior

### `records/forms.py`
- **Purpose**: Django forms for user input validation
- **Key Form: FileRecordForm**
  - Validates description (required, non-empty)
  - Validates file (required, max 10 MB)
  - Provides UI widgets and error messages
- **Modify**: To change validation rules or form fields

### `records/views.py`
- **Purpose**: Business logic for handling requests and responses
- **Key Functions**:
  - `list_records()`: Display records with search/filter/pagination
  - `upload_record()`: Handle file uploads
  - `download_file()`: Serve files for download
  - `delete_record()`: Delete records and files
  - `export_to_excel()`: Generate Excel export with current filters
- **Features**:
  - Search implementation (case-insensitive description matching)
  - Filter implementation (file type, date range)
  - Sort implementation (multiple sort options)
  - Excel generation with formatting
- **Modify**: To add features, change business logic, or modify filtering

### `records/urls.py`
- **Purpose**: URL routing for the records app
- **Endpoints**:
  - `/`: List view
  - `/upload/`: Upload handler
  - `/download/<id>/`: File download
  - `/delete/<id>/`: Record deletion
  - `/export/`: Excel export
- **Modify**: To add new endpoints or change URL patterns

### `records/admin.py`
- **Purpose**: Django admin interface configuration
- **Content**: Registers FileRecord model with admin panel
- **Features**:
  - List display columns
  - Searchable fields
  - Filterable fields
  - Read-only fields
- **Modify**: To customize admin interface

### `records/apps.py`
- **Purpose**: App configuration class
- **Content**: App metadata (name, default auto field)
- **Don't modify**: Usually not necessary

### `records/migrations/` Directory
- **Purpose**: Database migration files (created automatically)
- **Content**: Version-controlled database schema changes
- **Files**:
  - `__init__.py`: Makes directory a Python package
  - `0001_initial.py`: First migration (created by `makemigrations`)
  - `000X_*.py`: Subsequent migrations for schema changes
- **Don't modify**: Migrations are auto-generated

---

## `records/static/` Directory

Static files served to the browser (CSS, JavaScript, images).

### `records/static/css/style.css`
- **Purpose**: Complete stylesheet for the application
- **Key Features**:
  - CSS variables for consistent theming (colors, shadows, transitions)
  - Responsive grid layout
  - Table styling
  - Form styling
  - Button and badge styles
  - Modal dialog styling
  - Pagination styling
  - Mobile responsiveness (768px and 480px breakpoints)
  - Animations (slideIn, fadeIn, slideInUp)
- **Styling Classes**:
  - `.container`: Max-width wrapper
  - `.header`: Page header with gradient
  - `.upload-form`: File upload form styling
  - `.filter-form`: Search and filter form
  - `.records-table`: Data table
  - `.btn*`: Various button styles
  - `.badge*`: File type badges
  - `.modal`: Delete confirmation dialog
- **Modify**: To change colors, layout, or add new styles
- **Size**: ~8 KB

### `records/static/js/script.js`
- **Purpose**: Client-side JavaScript for interactivity
- **Key Functions**:
  - `deleteRecord(recordId)`: Show delete confirmation modal
  - `closeDeleteModal()`: Close confirmation dialog
  - Export functionality with loading state
  - Form validation
  - File input enhancement
- **Features**:
  - Delete confirmation with CSRF token
  - Modal dialog management
  - Export button state management
  - File input filename display
  - Form submission validation
- **Events**:
  - Click handlers for delete buttons
  - Submit handlers for forms
  - Window click handlers for modal dismiss
- **Modify**: To add new interactivity or change behaviors

---

## `records/templates/` Directory

HTML templates for rendering the user interface.

### `records/templates/records/list.html`
- **Purpose**: Main template for the entire application
- **Content**:
  - Meta tags and viewport configuration
  - Link to CSS stylesheet
  - Header with title
  - Message display area
  - Upload file form
  - Search and filter form
  - Records table with columns
  - Pagination controls
  - Delete confirmation modal
  - Script includes
- **Key Template Tags**:
  - `{% csrf_token %}`: CSRF protection
  - `{% if %}{% endif %}`: Conditional rendering
  - `{% for %}{% endfor %}`: Loop through records
  - `{{ variable }}`: Display variables
  - `{% url %}`: Generate URLs
  - `{{ value|filter }}`: Apply filters (date formatting, etc.)
- **Sections**:
  - Upload section: Simple file upload form
  - Search/Filter section: Advanced filtering options
  - Records section: Table with pagination
  - Delete modal: Confirmation dialog
- **Responsive**: Mobile-friendly layout
- **Modify**: To change UI structure or add new sections

---

## Database Files

### `db.sqlite3`
- **Purpose**: SQLite database file (created after first migration)
- **Content**: All application data (records, users)
- **Size**: Grows with uploaded files metadata
- **Backup**: Regularly backup this file
- **Don't modify**: Use Django admin or app interface

---

## Media Files

### `media/` Directory
- **Purpose**: Stores uploaded files
- **Structure**:
  - `uploads/`: Subdirectory containing all uploaded files
- **Content**: User-uploaded documents, images, etc.
- **Size**: Depends on uploaded files
- **Backup**: Important - contains all user data
- **Configuration**: `MEDIA_ROOT` in settings.py

### `media/uploads/`
- **Purpose**: Directory where files are actually stored
- **Naming**: Django uses original filename with optional suffix for duplicates
- **Permissions**: Should be readable by Django application
- **Cleanup**: Old files remain until explicitly deleted

---

## Summary Table

| File/Directory | Type | Purpose | Modify? |
|---|---|---|---|
| manage.py | Script | Django CLI | No |
| requirements.txt | Config | Dependencies | When adding packages |
| README.md | Docs | Main documentation | Yes |
| SETUP.md | Docs | Setup guide | Yes |
| QUICKSTART.txt | Docs | Quick start | Yes |
| config/settings.py | Config | Django settings | Yes (customization) |
| config/urls.py | Config | Main URL router | Yes (new features) |
| records/models.py | Code | Database models | Yes (new features) |
| records/forms.py | Code | Form validation | Yes (validation rules) |
| records/views.py | Code | Business logic | Yes (new features) |
| records/urls.py | Config | App URLs | Yes (new endpoints) |
| records/admin.py | Config | Admin interface | Yes (customization) |
| records/static/css/style.css | Styling | UI styling | Yes (design changes) |
| records/static/js/script.js | Script | Interactivity | Yes (new features) |
| records/templates/records/list.html | Template | UI template | Yes (layout changes) |
| records/migrations/*.py | Config | Schema changes | No (auto-generated) |
| db.sqlite3 | Database | Data storage | No (use interface) |
| media/uploads/ | Storage | User files | No (user data) |

---

## Creating New Features

### To Add a New Uploaded File Field:
1. Add field to `FileRecord` model in `records/models.py`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`

### To Add a New Filter:
1. Modify `list_records()` function in `records/views.py`
2. Add form field in `records/templates/records/list.html`
3. Add CSS styling if needed in `records/static/css/style.css`

### To Add a New Page:
1. Create new view in `records/views.py`
2. Create template in `records/templates/records/`
3. Add URL in `records/urls.py`
4. Link from existing pages in templates

### To Add a New API Endpoint:
1. Create view in `records/views.py` (use JsonResponse for API)
2. Add URL in `records/urls.py`
3. Call from JavaScript in `records/static/js/script.js`

---

**For detailed setup, see SETUP.md**  
**For quick start, see QUICKSTART.txt**  
**For general info, see README.md**
