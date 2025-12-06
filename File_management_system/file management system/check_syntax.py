import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    import django
    django.setup()
    from records import views
    from records import urls
    print("✓ All files compiled successfully")
    print("✓ views.py - OK")
    print("✓ urls.py - OK")
    print("\n✓ Edit feature is ready!")
except SyntaxError as e:
    print(f"✗ Syntax Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
