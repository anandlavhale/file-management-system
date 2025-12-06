#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print("\n" + "="*60)
print("DEPENDENCY VERIFICATION")
print("="*60 + "\n")

success = True

checks = [
    ("Django", "django"),
    ("XlsxWriter", "xlsxwriter"),
    ("python-dateutil", "dateutil"),
    ("Pillow", "PIL"),
]

for name, module in checks:
    try:
        mod = __import__(module)
        version = getattr(mod, "__version__", "unknown")
        print(f"✓ {name:<20} {version}")
    except ImportError as e:
        print(f"✗ {name:<20} FAILED - {e}")
        success = False

print("\n" + "="*60)
try:
    from records.views import export_to_excel
    print("✓ Export function imported successfully")
    print("="*60 + "\n")
    print("SUCCESS: All dependencies are properly installed!")
    print("The Excel export feature should work correctly.\n")
except Exception as e:
    print(f"✗ Export function import failed: {e}")
    print("="*60 + "\n")
    success = False

sys.exit(0 if success else 1)
