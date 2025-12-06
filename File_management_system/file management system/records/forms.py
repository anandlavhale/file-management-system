from django import forms
from .models import FileRecord


class FileRecordForm(forms.ModelForm):
    class Meta:
        model = FileRecord
        fields = ['description', 'file_date', 'letter_reference_number', 'file']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-input',
                'placeholder': 'Enter file description'
            }),
            'file_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
            }),
            'letter_reference_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter letter reference number (optional)'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-input',
                'accept': '*/*'
            }),
        }
    
    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()
        if not description:
            raise forms.ValidationError('Description cannot be empty.')
        return description
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise forms.ValidationError('Please select a file to upload.')
        if file.size > 10 * 1024 * 1024:
            raise forms.ValidationError('File size must not exceed 10 MB.')
        return file
