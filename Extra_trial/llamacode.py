import fitz
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def generate_llama3_response(text, query):
    prompt = f"Based on the following query, provide a the following from the text given after it: '{query}'. Here is the text: {text}"
    result = llm.invoke(prompt)
    return result

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def get_context(text, query):
    context = generate_llama3_response(text, query)
    return context

if __name__ == "__main__":
    pdf_path = "D:\\Professional Mobility\\Binocular Astronomy by Stephen Tonkin.pdf"
    text = extract_text_from_pdf(pdf_path)
    print("Enter your query for your task:")
    user_query = input().strip()

    context = get_context(text, user_query)
    print("Context based on your query:")
    print(context)