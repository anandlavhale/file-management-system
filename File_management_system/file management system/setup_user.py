import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

print("\n=== Setting up login user ===\n")

try:
    existing = User.objects.filter(username='MESGCC').first()
    if existing:
        print(f"✓ User 'MESGCC' already exists")
    else:
        print(f"Creating user 'MESGCC'...")
        User.objects.create_user(
            username='MESGCC',
            password='BBA@123'
        )
        print(f"✓ User 'MESGCC' created successfully")
    
    user = User.objects.get(username='MESGCC')
    print(f"\nUser Details:")
    print(f"  - Username: {user.username}")
    print(f"  - ID: {user.id}")
    print(f"  - Is active: {user.is_active}")
    
    from django.contrib.auth import authenticate
    test_user = authenticate(username='MESGCC', password='BBA@123')
    if test_user:
        print(f"\n✓ Authentication test PASSED")
    else:
        print(f"\n✗ Authentication test FAILED")
    
    print(f"\n=== Setup Complete ===")
    print(f"Login with:")
    print(f"  Username: MESGCC")
    print(f"  Password: BBA@123\n")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
