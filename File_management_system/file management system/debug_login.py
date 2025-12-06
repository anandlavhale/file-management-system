#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

print("\n" + "="*60)
print("LOGIN TROUBLESHOOTING")
print("="*60 + "\n")

try:
    from django.contrib.auth.models import User
    from records.signals import create_default_user
    
    print("1. Checking existing users in database:")
    users = User.objects.all()
    if users.exists():
        for user in users:
            print(f"   - Username: {user.username}, ID: {user.id}")
    else:
        print("   - No users found. Creating default user...")
        User.objects.create_user(username='MESGCC', password='BBA@123')
        print("   ✓ User 'MESGCC' created successfully")
    
    print("\n2. Verifying MESGCC user:")
    mesgcc = User.objects.filter(username='MESGCC').first()
    if mesgcc:
        print(f"   ✓ User exists: {mesgcc.username}")
        print(f"     - ID: {mesgcc.id}")
        print(f"     - Is active: {mesgcc.is_active}")
        print(f"     - Is staff: {mesgcc.is_staff}")
    else:
        print("   ✗ User MESGCC not found!")
        sys.exit(1)
    
    print("\n3. Testing authentication:")
    from django.contrib.auth import authenticate
    user = authenticate(username='MESGCC', password='BBA@123')
    if user is not None:
        print(f"   ✓ Authentication successful!")
    else:
        print(f"   ✗ Authentication failed!")
        sys.exit(1)
    
    print("\n4. Checking views import:")
    from records.views import login_view
    print("   ✓ login_view imported successfully")
    
    print("\n" + "="*60)
    print("✓ All checks passed! Login should work.")
    print("="*60)
    print("\nLogin credentials:")
    print("  Username: MESGCC")
    print("  Password: BBA@123")
    print("="*60 + "\n")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
