import pdfplumber

with pdfplumber.open("D:\\Professional Mobility\\Agricultural pattern.pdf") as pdf:
    pages = pdf.pages
    for page in pages:
        text = page.extract_text()

print(text) 