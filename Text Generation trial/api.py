import openai
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# OpenAI API key
openai.api_key = '33fb2db2f7864a6e8f5792f13b3aabd4 

'

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def generate_pdf(content, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []

    for item in content:
        if isinstance(item, str):
            flowables.append(Paragraph(item, styles['Normal']))
        flowables.append(Spacer(1, 12))

    doc.build(flowables)

prompt = "Generate an introduction for a presentation on the benefits of electric vehicles."
generated_text = generate_text(prompt)

content = [
    generated_text,
    "This is the second paragraph, which includes more information.",
]

generate_pdf(content, "presentation.ppt")
