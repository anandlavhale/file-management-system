import os
from django.db import models
from django.utils import timezone


class FileRecord(models.Model):
    FILE_TYPE_CHOICES = [
        ('PDF', 'PDF'),
        ('DOCX', 'DOCX'),
        ('XLSX', 'XLSX'),
        ('Image', 'Image'),
        ('Other', 'Other'),
    ]
    
    description = models.TextField(help_text="Description of the file")
    file = models.FileField(upload_to='uploads/')
    upload_datetime = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=20, choices=FILE_TYPE_CHOICES, default='Other')
    file_date = models.DateField(null=True, blank=True, help_text="Date associated with the file")
    letter_reference_number = models.CharField(max_length=255, null=True, blank=True, help_text="Letter or reference number")
    
    class Meta:
        ordering = ['-upload_datetime']
    
    def __str__(self):
        return f"{self.id} - {self.description[:50]}"
    
    def save(self, *args, **kwargs):
        if self.file:
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext == '.pdf':
                self.file_type = 'PDF'
            elif ext == '.docx':
                self.file_type = 'DOCX'
            elif ext == '.xlsx':
                self.file_type = 'XLSX'
            elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                self.file_type = 'Image'
            else:
                self.file_type = 'Other'
        super().save(*args, **kwargs)
    
    @property
    def file_name(self):
        return os.path.basename(self.file.name)
