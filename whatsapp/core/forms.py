from django import forms

class UploadDataForm(forms.Form):
    excel_file = forms.FileField()