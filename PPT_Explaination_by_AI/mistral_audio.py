# Final codde for audio explaination

import os
from langchain_community.llms import Ollama
from gtts import gTTS

generator = Ollama(model='mistral')

def generate_slide_content(prompt):
    result = generator.invoke(prompt)
    
    print("Result from generator.invoke(prompt):", result)
    
    if isinstance(result, str):
        return result.strip()
    
    if isinstance(result, dict) and 'text' in result:
        return result['text'].strip()
    
    raise TypeError(f"Unexpected result format: {type(result)}")

def generate_voiceover(text, audio_file):
    tts = gTTS(text, lang='en')
    tts.save(audio_file)

def create_audio_for_prompts(prompts):
    for i, prompt in enumerate(prompts):
        content = generate_slide_content(prompt)
        generate_voiceover(content, f'audio_mistral_{i}.mp3')

prompts = [
    "Explain the importance of AI in modern technology.",
    "Describe how machine learning algorithms work.",
    "Summarize the key takeaways from AI advancements."
]

create_audio_for_prompts(prompts)