from django.shortcuts import render, HttpResponse
from .models import Document
from .forms import DocumentForm
import io
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import arabic_reshaper
from bidi.algorithm import get_display
from docx import Document as DocxDocument
import arabic_reshaper


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['docfile']
            print(f"Uploaded file: {uploaded_file.name}")
            output_file = perform_ocr(uploaded_file)
            print(f"OCR output saved to {output_file}")
            
            if output_file is None:
                print("Error during OCR process")
                return HttpResponse("Error during OCR process")
            
            # Return the text file to the user for download with explicit UTF-8 encoding
            with open(output_file, 'rb') as f:
                response = HttpResponse(f.read(), content_type='text/plain; charset=utf-8')
                response['Content-Disposition'] = f'attachment; filename="{output_file}"'
                print("Returning response")
                return response
            
        else:
            print("Invalid file format")
            return HttpResponse("Invalid file format. Only images (jpg, jpeg, png, gif) and PDFs are supported.")
            
    else:
        form = DocumentForm()

    return render(request, 'ocr_app/upload.html', {'form': form})




import io
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import arabic_reshaper
from bidi.algorithm import get_display
from docx import Document as DocxDocument
import io
from PIL import Image
import pytesseract
import arabic_reshaper
from bidi.algorithm import get_display
from docx import Document as DocxDocument

import fitz  # PyMuPDF
def perform_ocr(file):
    try:
        file_extension = file.name.split('.')[-1].lower()
        docx = DocxDocument()  # Create a new Word document

        if file_extension == 'pdf':
            print("Performing OCR on each page in the PDF file...")
            pdf_document = fitz.open(stream=file.read(), filetype="pdf")
            for page in pdf_document:
                for line in page.get_text("text").split('\n'):
                    # Reshape and reorder Arabic text
                    line = arabic_reshaper.reshape(line)
                    docx.add_paragraph(line)
            output_file = "output.docx"
            docx.save(output_file)
            
        else:
            print("Invalid file format")
            return None

        print("OCR process completed.")
        return output_file
    except Exception as e:
        print(f"Error during OCR process: {e}")
        return None
