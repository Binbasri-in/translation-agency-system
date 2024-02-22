from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    input_file_type = forms.ChoiceField(
        choices=[('pdf', 'PDF'), ('image', 'Image')],
        label='Input File Type',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    output_file_type = forms.ChoiceField(
        choices=[('txt', 'Text'), ('docx', 'Word Document'), ('xlsx', 'Excel Sheet')],
        label='Output File Type',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
