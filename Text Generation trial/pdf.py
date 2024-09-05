# import fitz  

# def extract_text_from_pdf(pdf_path):
#     pdf_document = fitz.open(pdf_path)
    
#     extracted_text = ""

#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)  
#         extracted_text += page.get_text()  
#     return extracted_text

# pdf_path = "D:\Text Generation\Binocular Astronomy by Stephen Tonkin.pdf"

# text = extract_text_from_pdf(pdf_path)

# print(text)

import requests

api_key = '0886b8a3-b079-4d20-b474-eac740d18fdc'
api_url = 'https://api.powerpointgeneratorapi.com/generate'

payload = {
    'title': 'Sample Presentation',
    'slides': [
        {
            'title': 'Slide 1 Title',
            'content': 'This is the content of the first slide'
        },
        {
            'title': 'Slide 2 Title',
            'content': 'This is the content of the second slide'
        }
    ]
}

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(api_url, json=payload, headers=headers)

# if response.status_code == 200:
with open('presentation.pptx', 'wb') as f:
    f.write(response.content)
print('Presentation created successfully.')
# else:
    # print('Failed to create presentation:', response.text)
