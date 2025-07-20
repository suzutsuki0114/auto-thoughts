import PyPDF2
from pathlib import Path

class PDFToTextConverter:
    def pdf_to_text(self, document_path):
        path = Path(document_path)
        with open(path, 'rb') as pdf_file:

            pdf_reader = PyPDF2.PdfReader(pdf_file)

            full_text = ""
            for page in pdf_reader.pages:
                full_text += page.extract_text() + "\n"

            return full_text
