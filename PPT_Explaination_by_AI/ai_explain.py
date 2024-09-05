import os
from transformers import pipeline
from moviepy.editor import ImageSequenceClip, VideoFileClip, AudioFileClip
from gtts import gTTS

generator = pipeline('text-generation', model='gpt2')

def generate_slide_content(prompt):
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text'].strip()


def create_video_from_images(image_folder, output_file, fps=1):
    image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith('.png')]
    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(output_file, codec="libx264")

def generate_voiceover(text, audio_file):
    tts = gTTS(text, lang='en')
    tts.save(audio_file)

def add_voiceover_to_video(video_file, audio_file, output_file):
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    video = video.set_audio(audio)
    video.write_videofile(output_file, codec="libx264")

prompts = [
    "Explain the importance of AI in modern technology.",
    "Describe how machine learning algorithms work.",
    "Summarize the key takeaways from AI advancements."
]

for i, prompt in enumerate(prompts):
    content = generate_slide_content(prompt)
    generate_voiceover(content, f'voiceover_{i}.mp3')

create_video_from_images('output_images', 'presentation_video.mp4')


















































































# import openai

# openai.api_key = 'sk-0bp9BdYbqLGQiEnvNz4t7EhWetuOvmqkEXSsBMFuMFT3BlbkFJ4345YLyZOANUuKRgQCDMZfWD_n6IilCPhixlBYMFUA'

# def generate_slide_content(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

# from pptx import Presentation

# prs = Presentation()
# def add_slide(title, content):
#     slide_layout = prs.slide_layouts[1]  
#     slide = prs.slides.add_slide(slide_layout)
#     title_placeholder = slide.shapes.title
#     content_placeholder = slide.placeholders[1]

#     title_placeholder.text = title
#     content_placeholder.text = content

# titles = ["Introduction"]
# prompts = ["You are an educational content expert tasked with creating a complete course based on the following subtopics: Artificial Intelligence. Your goal is to generate a well-structured course that is necessary for me to understand the topic completely. Please create a comprehensive course that incorporates these subtopics, ensuring that the course is relevant, comprehensive, and engaging for Beginner -level learners. Include learning objectives, key concepts,and practical applications methods for each subtopic."]

# for title, prompt in zip(titles, prompts):
#     content = generate_slide_content(prompt)
#     add_slide(title, content)

# prs.save('Ai_presentation.pptx')
