# import requests

# url = "https://auth.powerpointgeneratorapi.com/v1.0/token/create"

# credentials = {
#     'username': '<your_username>',
#     'password': '<your_password>',
#     'key': '<your_security_key>'
# }

# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded'
# }

# response = requests.post(url, headers=headers, data=credentials)

# print(response.text)

import requests

# payload={'jsonData': '{"template":"title_slide_template.pptx","export_version":"Pptx2010","resultFileName":"quick_start_example","slides":[{"type":"slide","slide_index":0,"shapes":[{"name":"Title 1","content":"Your generated PowerPoint presentation"},{"name":"Subtitle 2","content":"Create, fill and manage PowerPoint documents through simple API requests."}]}]}'}
payload = {'jsonData': '{"template":"D:\Text Generation trial\ACIDS, BASES AND SALTS.pptx","export_version":"Pptx2010","resultFileName":"python_presentation","slides":[{"type":"slide","slide_index":0,"shapes":[{"name":"Title 1","content":"Introduction to Python"},{"name":"Subtitle 2","content":"A versatile programming language for various applications."}]},{"type":"slide","slide_index":1,"shapes":[{"name":"Title 1","content":"Python Basics"},{"name":"Content 1","content":"Python is an interpreted, high-level, and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Pythons design philosophy emphasizes code readability with its notable use of significant whitespace."}]},{"type":"slide","slide_index":2,"shapes":[{"name":"Title 1","content":"Key Features of Python"},{"name":"Content 1","content":"1. Easy to Learn and Use\n2. Expressive Language\n3. Interpreted Language\n4. Cross-platform Language\n5. Free and Open Source\n6. Object-Oriented Language\n7. Extensible\n8. Large Standard Library\n9. GUI Programming Support\n10. Integrated"}]},{"type":"slide","slide_index":3,"shapes":[{"name":"Title 1","content":"Popular Python Libraries"},{"name":"Content 1","content":"1. NumPy\n2. Pandas\n3. Matplotlib\n4. SciPy\n5. Scikit-Learn\n6. TensorFlow\n7. Keras\n8. Flask\n9. Django\n10. Requests"}]}]}'}

files=[
  ('files', ('title_slide_template.pptx', open('D:\Text Generation trial\ACIDS, BASES AND SALTS.pptx','rb'), 'application/vnd.openxmlformats-officedocument.presentationml.presentation'))
]

response = requests.post(
    'https://gen.powerpointgeneratorapi.com/v1.0/generator/create',
    data=payload,
    files=files,
    headers={
        'Authorization': f'Bearer <0886b8a3-b079-4d20-b474-eac740d18fdc>',
    },
    timeout=360
)

with open("./generated.pptx", "wb") as file:
    file.write(response.content)