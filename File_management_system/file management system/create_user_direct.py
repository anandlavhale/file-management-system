#!/usr/bin/env python
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.contrib.auth.models import User

print("\n" + "="*60)
print("CREATING LOGIN USER")
print("="*60 + "\n")

try:
    User.objects.filter(username='MESGCC').delete()
    print("Deleted old user if it existed...")
    
    user = User.objects.create_user(
        username='MESGCC',
        password='BBA@123',
        is_active=True
    )
    print(f"✓ User created successfully!")
    print(f"\nUser Details:")
    print(f"  Username: {user.username}")
    print(f"  ID: {user.id}")
    print(f"  Is Active: {user.is_active}")
    
    from django.contrib.auth import authenticate
    auth_user = authenticate(username='MESGCC', password='BBA@123')
    
    if auth_user:
        print(f"\n✓ Authentication TEST PASSED!")
    else:
        print(f"\n✗ Authentication TEST FAILED!")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("SUCCESS! You can now login with:")
    print("  Username: MESGCC")
    print("  Password: BBA@123")
    print("="*60 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {e}\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)
