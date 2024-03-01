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


class TranslationForm(forms.Form):
    text = forms.CharField(
        label='Enter text to translate',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    source_lang = forms.ChoiceField(
        choices=[('arabic', 'Arabic'), ('english', 'English'), ('french', 'French'), ('spanish', 'Spanish')],
        label='Source Language',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    target_lang = forms.ChoiceField(
        choices=[('arabic', 'Arabic'), ('english', 'English'), ('french', 'French'), ('spanish', 'Spanish')],
        label='Target Language',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    