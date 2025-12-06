# File Management System

A complete fullstack file management application built with Django, vanilla JavaScript, and SQLite3. Upload, manage, search, filter, and export your files with an intuitive web interface.

## 🚀 Quick Start

### Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Then open `http://localhost:8000` in your browser.

**→ See QUICKSTART.txt for even faster setup!**

## ✨ Features

| Feature | Description |
|---------|-------------|
| **📤 File Upload** | Upload files with automatic file type detection |
| **🔍 Smart Search** | Search descriptions with case-insensitive, partial matching |
| **🎯 Advanced Filters** | Filter by file type, date range, with multiple sort options |
| **📊 Export to Excel** | Export filtered results directly to XLSX format |
| **📥 Download Files** | Download uploaded files with a single click |
| **🗑️ Delete Records** | Remove records with confirmation dialog |
| **📄 Pagination** | Navigate through 10 records per page |
| **📱 Responsive** | Works on desktop, tablet, and mobile devices |
| **💾 SQLite Database** | No complex database setup required |

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)
- Modern web browser
- ~50 MB disk space

## 🛠️ Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite3
- **Excel Export**: openpyxl 3.11.0

## 📂 Project Structure

```
file management system/
├── config/                      # Django project settings
│   ├── settings.py             # Main configuration
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py
├── records/                    # Main Django application
│   ├── migrations/             # Database migrations
│   ├── static/
│   │   ├── css/style.css       # Responsive styling
│   │   └── js/script.js        # Client-side interactivity
│   ├── templates/records/
│   │   └── list.html           # Main UI template
│   ├── models.py               # Database models (FileRecord)
│   ├── views.py                # View logic
│   ├── urls.py                 # App URL routing
│   ├── forms.py                # Upload form validation
│   ├── admin.py                # Django admin config
│   └── apps.py
├── media/                      # Uploaded files directory
├── manage.py                   # Django CLI
├── requirements.txt            # Python dependencies
├── SETUP.md                    # Detailed setup guide
├── QUICKSTART.txt             # Quick start guide
└── README.md                   # This file
```

## 🎯 Features in Detail

### 1. Upload Files
- Fill in file description (required)
- Select any file type (PDF, DOCX, XLSX, Images, etc.)
- Max file size: 10 MB
- Automatic file type detection

### 2. Search & Filter
- **Search**: Find records by description text (case-insensitive)
- **Filter by Type**: PDF, DOCX, XLSX, Image, Other
- **Date Range**: Filter by upload date range
- **Sort Options**:
  - Newest first / Oldest first
  - Description A-Z / Z-A

### 3. Export to Excel
- Export visible/filtered records
- Includes: S.No, Description, File Name, Type, Upload Date & Time
- Professional Excel formatting with headers

### 4. Record Management
- **Download**: Get your files directly
- **Delete**: Remove records with confirmation
- **Pagination**: Easy navigation through records

## 📊 Database

**Model: FileRecord**
```python
- id (Primary Key)
- description (Text)
- file (FileField)
- upload_datetime (DateTime, auto-set)
- file_type (Auto-detected: PDF, DOCX, XLSX, Image, Other)
```

## 🔧 Installation

See **SETUP.md** for comprehensive installation and configuration instructions.

### Quick Summary:
1. Create virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Start server: `python manage.py runserver`
5. Visit `http://localhost:8000`

## 📝 Usage Guide

### Uploading a File
1. Fill in the description field
2. Select a file from your computer
3. Click "Upload File"
4. See success message and your file in the table

### Searching Records
1. Enter search text in the "Search Description" field
2. Click "Apply Filters"
3. Results update to show matching records

### Filtering Records
1. Select file type, date range, or sort order
2. Combine filters as needed
3. Click "Apply Filters"
4. Clear any filter with "Clear Filters" button

### Exporting Data
1. Apply desired filters/search (optional)
2. Click "Export to Excel"
3. File downloads automatically as `file_records.xlsx`

### Managing Files
- **Download**: Click download button to get the file
- **Delete**: Click delete, confirm in dialog, record and file removed

## 🌐 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | List records, search, filter |
| POST | `/upload/` | Upload new file |
| GET | `/download/<id>/` | Download file |
| POST | `/delete/<id>/` | Delete record |
| GET | `/export/` | Export filtered results to Excel |

## 🔒 Security Features

- CSRF protection enabled
- Server-side file upload validation
- File type verification
- File size limits (10 MB default)
- SQL injection protection (Django ORM)
- Secure file storage outside web root

## ⚙️ Configuration

### Change Upload Directory
Edit `records/models.py`:
```python
file = models.FileField(upload_to='uploads/')  # Change this path
```

### Change Records Per Page
Edit `records/views.py`:
```python
paginator = Paginator(records, 10)  # Change 10 to desired number
```

### Change Max File Size
Edit `config/settings.py`:
```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB in bytes
```

## 🐛 Troubleshooting

### Database Issues
```bash
# Reset everything
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
```

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### Static Files Not Loading
```bash
# Development (automatic)
python manage.py runserver

# Production
python manage.py collectstatic
```

See **SETUP.md** for more troubleshooting solutions.

## 📈 Performance

- Pagination for efficient data loading
- Database indexing on frequently filtered fields
- Query optimization through Django ORM
- Client-side form validation reduces server load
- Responsive CSS with minimal external dependencies

## 🎨 UI/UX Highlights

- **Modern Design**: Clean, professional interface
- **Responsive**: Works seamlessly on all screen sizes
- **Accessibility**: WCAG compliant (keyboard navigation, color contrast)
- **User Feedback**: Toast messages for all actions
- **Loading States**: Visual feedback during operations
- **Dark Mode Ready**: CSS can be extended for dark theme

## 🚀 Production Deployment

Before deploying:
1. Change `SECRET_KEY` in `config/settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Use PostgreSQL instead of SQLite
5. Set up proper static/media file serving (nginx, etc.)
6. Enable HTTPS
7. Set up environment variables for sensitive data

## 📦 Dependencies

```
Django==4.2.7          # Web framework
openpyxl==3.1.5        # Excel file generation
python-dateutil==2.8.2 # Date utilities
```

## 📄 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Feel free to fork, modify, and extend this project for your needs.

## ❓ FAQ

**Q: Can I change the allowed file types?**  
A: Yes, modify the `FILE_TYPE_CHOICES` in `records/models.py`

**Q: Can I disable file size limits?**  
A: Yes, remove file size validation from `records/forms.py` and increase `FILE_UPLOAD_MAX_MEMORY_SIZE`

**Q: Can I use this with PostgreSQL?**  
A: Yes, change `DATABASES` setting in `config/settings.py`

**Q: How do I backup my data?**  
A: Backup the `db.sqlite3` file and `media/` directory

**Q: Can I host this online?**  
A: Yes, use platforms like Heroku, PythonAnywhere, or your own server

## 📞 Support

For issues:
1. Check the **SETUP.md** troubleshooting section
2. Review [Django Documentation](https://docs.djangoproject.com/)
3. Check [openpyxl Documentation](https://openpyxl.readthedocs.io/)

---

**Ready to get started?** See **QUICKSTART.txt** for the fastest setup!
