@echo off
cd /d "d:\file management system"
python manage.py migrate
python create_user_direct.py
pause
