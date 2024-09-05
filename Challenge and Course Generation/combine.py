# # Import required modules
# import re
# import csv
# import integrated_function
# from Subtopic_Challenge import model3_list 
# import os
# from langchain_community.llms import Ollama
# from gtts import gTTS

# generator = Ollama(model='mistral')

# def generate_slide_content(prompt):
#     result = generator.invoke(prompt)
    
#     print("Result from generator.invoke(prompt):", result)
    
#     if isinstance(result, str):
#         return result.strip()
    
#     if isinstance(result, dict) and 'text' in result:
#         return result['text'].strip()
    
#     raise TypeError(f"Unexpected result format: {type(result)}")

# def generate_voiceover(text, audio_file):
#     tts = gTTS(text, lang='en')
#     tts.save(audio_file)

# def create_audio_for_prompts(prompts):
#     for i, prompt in enumerate(prompts):
#         content = generate_slide_content(prompt)
#         generate_voiceover(content, f'audio_mistral_{i}.mp3')

# def create_custom_prompts(subtopics, levels):
#     base_prompt = """Provide a comprehensive audio explanation of the course content based on the following subtopics: {s_topics}. The course is designed for {levels}-level learners. 
#     Include in your explanation the following elements for each subtopic: 
#     1. Learning Objectives: Clearly state the goals and what learners are expected to achieve.
#     2. Key Concepts: Outline the fundamental ideas and principles that need to be understood.
#     3. Practical Applications: Describe how the concepts can be applied in real-world scenarios.
#     4. Engagement Strategies: Suggest methods to make the learning experience more interactive and engaging.

#     Ensure the explanation is clear, detailed, and suitable for learners at the specified level. Aim for an informative and engaging delivery that facilitates a thorough understanding of each topic."""
    
#     prompt = base_prompt.format(s_topics=subtopics, levels=levels)
#     return [prompt]  

# subtopics = "Data Science Fundamentals, Machine Learning Basics, Model Evaluation"
# levels = "intermediate"

# prompts = create_custom_prompts(subtopics, levels)
# create_audio_for_prompts(prompts)


import os
from langchain_community.llms import Ollama
from google.cloud import texttospeech

generator = Ollama(model='llama3')

def generate_slide_content(prompt):
    result = generator.invoke(prompt)
    
    print("Result from generator.invoke(prompt):", result)
    
    if isinstance(result, str):
        return result.strip()
    
    if isinstance(result, dict) and 'text' in result:
        return result['text'].strip()
    
    raise TypeError(f"Unexpected result format: {type(result)}")

def generate_voiceover(text, audio_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        name="en-US-Wavenet-D"  
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(audio_file, "wb") as out:
        out.write(response.audio_content)

def create_audio_for_prompts(prompts):
    for i, prompt in enumerate(prompts):
        content = generate_slide_content(prompt)
        generate_voiceover(content, f'audio_llama3_{i}.mp3')

prompts = [
    "Explain the importance of AI in modern technology.",
    "Describe how machine learning algorithms work.",
    "Summarize the key takeaways from AI advancements."
]

create_audio_for_prompts(prompts)