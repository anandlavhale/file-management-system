# File Management System - Setup Instructions

A complete fullstack file management application built with Django, vanilla JavaScript, and SQLite3.

## Features

- **File Upload & Management**: Upload files with descriptions and automatic file type detection
- **Search**: Case-insensitive search on description field
- **Advanced Filters**: 
  - Date range filtering (from/to dates)
  - File type filtering (PDF, DOCX, XLSX, Image, Other)
  - Multiple sort options (newest/oldest, A-Z/Z-A)
- **Export**: Export filtered records to Excel format
- **Pagination**: Paginated table view (10 records per page)
- **Responsive UI**: Clean, modern, mobile-friendly interface
- **CRUD Operations**: View, Download, and Delete records

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- Modern web browser

## Installation & Setup

### WINDOWS - Step by Step:

**Step 1: Navigate to project directory**
```bash
cd d:\file management system
```

**Step 2: Create virtual environment**
```bash
python -m venv venv
```

**Step 3: Activate virtual environment**
```bash
venv\Scripts\activate
```
You should see `(venv)` at the start of your command line.

**Step 4: Install all dependencies**
```bash
pip install -r requirements.txt
```
Wait for completion. You should see "Successfully installed Django, XlsxWriter, python-dateutil..."

**Step 5: Create database and run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 6: Run development server**
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

---

### MAC/LINUX - Step by Step:

**Step 1: Navigate to project directory**
```bash
cd path/to/file\ management\ system
```

**Step 2: Create virtual environment**
```bash
python3 -m venv venv
```

**Step 3: Activate virtual environment**
```bash
source venv/bin/activate
```
You should see `(venv)` at the start of your command line.

**Step 4: Install all dependencies**
```bash
pip install -r requirements.txt
```
Wait for completion.

**Step 5: Create database and run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 6: Run development server**
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

---

### Create Superuser (Optional but Recommended)

In a new terminal (keeping the server running), activate venv again then:
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account. Access it at `http://localhost:8000/admin/`

## Login Credentials

The system is protected with authentication. Use the following credentials to login:

- **Username**: `MESGCC`
- **Password**: `BBA@123`

**Note**: The user account is automatically created when you run migrations for the first time.

## Usage

### Login & Authentication
- Open the application in your browser (e.g., `http://localhost:8000/`)
- You will be redirected to the login page
- Enter the username and password above
- Click "Login" to access the dashboard
- Click "Logout" button in the header to log out

### Main Dashboard
- **Upload Form**: Fill in description and select a file, then click "Upload File"
- **Search**: Enter text in the search box to filter by description
- **Filters**: 
  - Select a file type from dropdown
  - Choose date range with calendar pickers
  - Select sort order
  - Click "Apply Filters" to apply all filters
- **Clear Filters**: Click the "Clear Filters" button to reset all search/filter parameters
- **Export**: Click "Export to Excel" to download current filtered results

### Table Actions
- **Edit**: Click the Edit button to modify record details (description, file date, letter reference number)
- **Download**: Click the Download button to download a file
- **Delete**: Click the Delete button and confirm to remove a record

### Pagination
- Navigate between pages using First, Previous, Next, and Last buttons
- Page information shows current page and total pages

## Project Structure

```
file management system/
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── SETUP.md                           # This file
├── db.sqlite3                         # SQLite database (created after migration)
│
├── config/                            # Django project settings
│   ├── __init__.py
│   ├── settings.py                    # Project configuration
│   ├── urls.py                        # Main URL routing
│   ├── wsgi.py                        # WSGI application
│
├── records/                           # Main Django app
│   ├── migrations/                    # Database migrations (created after migration)
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css             # Main stylesheet
│   │   └── js/
│   │       └── script.js             # JavaScript for interactivity
│   ├── templates/
│   │   └── records/
│   │       └── list.html             # Main template
│   │
│   ├── __init__.py
│   ├── admin.py                      # Django admin configuration
│   ├── apps.py                       # App configuration
│   ├── forms.py                      # Django forms
│   ├── models.py                     # Database models
│   ├── urls.py                       # App URL routing
│   └── views.py                      # View functions
│
└── media/                             # Uploaded files directory (created on first upload)
```

## Models

### FileRecord Model

```python
Fields:
- id (Auto-increment primary key)
- description (TextField) - Description of the file
- file (FileField) - The uploaded file
- upload_datetime (DateTimeField) - Auto-set to current time on upload
- file_type (CharField) - Auto-detected from file extension
  - Options: PDF, DOCX, XLSX, Image, Other
```

## API Endpoints

| Method | URL | Function |
|--------|-----|----------|
| GET | `/` | List records with search/filters |
| POST | `/upload/` | Upload new file |
| GET | `/download/<id>/` | Download a file |
| POST | `/delete/<id>/` | Delete a record |
| GET | `/export/` | Export filtered records to Excel |

## Configuration

### File Upload Settings
- **Max File Size**: 10 MB (configurable in `settings.py`)
- **Upload Directory**: `media/uploads/`
- **Allowed Extensions**: All file types

### Pagination
- **Records per Page**: 10 (configurable in `views.py`)

## Dependencies

- **Django 4.2.7**: Web framework
- **XlsxWriter 3.1.9**: Excel file generation
- **python-dateutil 2.8.2**: Date handling
- **Pillow 12.0.0**: Image processing

## Database

The application uses **SQLite3** (default Django database), stored in `db.sqlite3`.

### To Reset Database:
```bash
# Delete the database file
rm db.sqlite3

# Recreate migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## Common Issues & Troubleshooting

### Issue: ModuleNotFoundError: No module named 'django'
**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Database migration errors
**Solution**: Run migrations in order
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: For development, Django serves static files automatically. For production, run:
```bash
python manage.py collectstatic
```

### Issue: File not downloading properly
**Solution**: Ensure media directory exists and has proper permissions

### Issue: Excel export not working (ModuleNotFoundError: No module named 'xlsxwriter')
**Solution**: Verify XlsxWriter is installed
```bash
pip install xlsxwriter
```
Or reinstall all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Login page appears but "Invalid credentials" error
**Solution**: Ensure migrations have been run to create the user
```bash
python manage.py makemigrations
python manage.py migrate
```
Then use credentials:
- Username: `MESGCC`
- Password: `BBA@123`

### Issue: Redirected to login page when accessing pages
**Solution**: This is expected behavior. The application requires authentication. Simply log in with the credentials provided.

### Issue: Lost login credentials or need to reset
**Solution**: Delete the database and run migrations again to recreate the default user
```bash
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

## Development Notes

### Adding New File Types
Edit `records/models.py` in the `FileRecord` model's `save()` method to add new file type detection.

### Customizing Pagination
Edit `RECORDS_PER_PAGE` constant in `records/views.py`

### Changing Upload Directory
Edit `upload_to='uploads/'` in `records/models.py` or modify `MEDIA_ROOT` in `config/settings.py`

## Security Considerations

- **Authentication**: All pages require login with username and password
- **Session Management**: User sessions are managed by Django's authentication system
- **CSRF Protection**: CSRF protection is enabled on all forms
- **File uploads are stored in `media/` directory which is outside the Django app
- Validation is performed on both frontend and backend
- File extensions are validated
- File size limits are enforced (10 MB default)
- User credentials are securely stored using Django's password hashing

## Performance Tips

1. **Pagination**: The app uses pagination to handle large datasets efficiently
2. **Database Indexing**: Indexes are automatically created on common filter fields
3. **Query Optimization**: Only necessary fields are selected in queries

## Production Deployment

### Before deploying to production:

1. Change `SECRET_KEY` in `config/settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Configure static and media files on your web server
6. Set up proper file permissions
7. Use environment variables for sensitive settings
8. Enable HTTPS

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Django documentation: https://docs.djangoproject.com/
3. Check openpyxl documentation: https://openpyxl.readthedocs.io/

## License

This project is open source and available for educational purposes.
