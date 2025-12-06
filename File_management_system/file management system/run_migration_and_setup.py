import os
import sys
import subprocess

os.chdir(r'd:\file management system')
sys.path.insert(0, r'd:\file management system')

print("\n" + "="*70)
print("RUNNING DJANGO SETUP")
print("="*70 + "\n")

print("Step 1: Running migrations...\n")
result = subprocess.run([sys.executable, 'manage.py', 'migrate'], capture_output=False)
if result.returncode != 0:
    print("\n[FAILED] Migrations failed!")
    sys.exit(1)

print("\n" + "-"*70)
print("Step 2: Creating login user...\n")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

try:
    User.objects.filter(username='MESGCC').delete()
    print("[OK] Cleaned up old user...")
    
    user = User.objects.create_user(
        username='MESGCC',
        password='BBA@123',
        is_active=True
    )
    print("[OK] User 'MESGCC' created successfully!")
    
    auth_user = authenticate(username='MESGCC', password='BBA@123')
    if auth_user:
        print("[OK] Authentication test PASSED!\n")
    else:
        print("[FAILED] Authentication test FAILED!\n")
        sys.exit(1)
    
    print("="*70)
    print("SUCCESS! Setup complete.")
    print("\nYou can now login with:")
    print("  Username: MESGCC")
    print("  Password: BBA@123")
    print("="*70 + "\n")
    
except Exception as e:
    print("[ERROR] " + str(e) + "\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)
