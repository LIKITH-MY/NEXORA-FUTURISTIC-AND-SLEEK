# PDF extraction logic
from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    except:
        return ""
