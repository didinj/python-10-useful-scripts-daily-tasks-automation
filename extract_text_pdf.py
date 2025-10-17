import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf:
        reader = PyPDF2.PdfReader(pdf)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Example usage
# print(extract_text_from_pdf("example.pdf"))
