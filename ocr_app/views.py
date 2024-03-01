from django.shortcuts import render, HttpResponse
from .forms import DocumentForm, TranslationForm
from .utils import perform_ocr_image_to_text, perform_ocr_image_to_docx, perform_ocr_image_to_xlsx, perform_ocr_pdf_to_docx, perform_ocr_pdf_to_text, perform_ocr_pdf_to_xlsx
from .utils import translate_text_cloudflare


# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            input_file_type = form.cleaned_data['input_file_type']
            print(f"Input file type: {input_file_type}")
            output_file_type = form.cleaned_data['output_file_type']
            print(f"Output file type: {output_file_type}")
            uploaded_file = request.FILES['docfile']
            print(f"Uploaded file: {uploaded_file.name}")

            # confirm that the file is a PDF or an image
            file_extension = uploaded_file.name.split('.')[-1].lower()
            if file_extension not in ['pdf', 'jpg', 'jpeg', 'png']:
                error_message = "Invalid file format. Only PDFs and images are supported."
                return render(request, 'ocr_app/upload.html', {'form': form, 'error': error_message})

            # Perform OCR on the uploaded file
            if input_file_type == 'pdf' and output_file_type == 'docx':
                output_file = perform_ocr_pdf_to_docx(uploaded_file)
            elif input_file_type == 'pdf' and output_file_type == 'txt':
                output_file = perform_ocr_pdf_to_text(uploaded_file)
            elif input_file_type == 'pdf' and output_file_type == 'xlsx':
                output_file = perform_ocr_pdf_to_xlsx(uploaded_file)
            elif input_file_type == 'image' and output_file_type == 'docx':
                output_file = perform_ocr_image_to_docx(uploaded_file)
            elif input_file_type == 'image' and output_file_type == 'txt':
                output_file = perform_ocr_image_to_text(uploaded_file)
            elif input_file_type == 'image' and output_file_type == 'xlsx':
                output_file = perform_ocr_image_to_xlsx(uploaded_file)
            else:
                error_message = "Invalid combination of input and output file types."
                return render(request, 'ocr_app/upload.html', {'form': form, 'error': error_message})

            print(f"OCR output saved to {output_file}")

            if output_file is None:
                print("Error during OCR process")
                error_message = "Error during OCR process"
                return render(request, 'ocr_app/upload.html', {'form': form, 'error': error_message})

            # Return the text file to the user for download with explicit UTF-8 encoding
            with open(output_file, 'rb') as f:
                response = HttpResponse(f.read(), content_type='text/plain; charset=utf-8')
                response['Content-Disposition'] = f'attachment; filename="{output_file}"'
                print("Returning response")
                return response
        else:
            error_message = "Invalid file format. Only PDFs or Images are supported."
            return render(request, 'ocr_app/upload.html', {'form': form, 'error': error_message})
    else:
        error_message = ""

    form = DocumentForm()

    return render(request, 'ocr_app/upload.html', {'form': form, 'error': error_message})


def translate_text(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            source_lang = form.cleaned_data['source_lang']
            target_lang = form.cleaned_data['target_lang']
            print(f"Translating text from {source_lang} to {target_lang}")
            translated_text = translate_text_cloudflare(text, source_lang, target_lang)
            print(f"Translated text: {translated_text}")
        else:
            translated_text = ""
    else:
        translated_text = ""
        form = TranslationForm()
        
    return render(request, 'ocr_app/translate.html', {'form': form, 'translated_text': translated_text})