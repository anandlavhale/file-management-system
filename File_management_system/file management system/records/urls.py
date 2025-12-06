from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.list_records, name='list_records'),
    path('upload/', views.upload_record, name='upload_record'),
    path('edit/<int:record_id>/', views.edit_record, name='edit_record'),
    path('download/<int:record_id>/', views.download_file, name='download_file'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('export/', views.export_to_excel, name='export_to_excel'),
]
