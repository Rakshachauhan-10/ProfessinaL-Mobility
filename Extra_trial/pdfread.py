import fitz  

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    
    extracted_text = ""

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  
        extracted_text += page.get_text()  
    return extracted_text

pdf_path = "D:\\Professional Mobility\\Agricultural pattern.pdf"

text = extract_text_from_pdf(pdf_path)
print(text)