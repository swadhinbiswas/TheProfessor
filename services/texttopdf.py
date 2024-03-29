from pypdf import PdfReader

def pdftotext(file):
    with open(file, 'rb') as f:
        reader = PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
