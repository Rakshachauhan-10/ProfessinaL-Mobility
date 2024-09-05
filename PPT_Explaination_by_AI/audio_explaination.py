import os
from transformers import pipeline
from gtts import gTTS

generator = pipeline('text-generation', model='gpt2')

def generate_slide_content(prompt):
    result = generator(prompt, max_length=150, num_return_sequences=1)
    return result[0]['generated_text'].strip()

def generate_voiceover(text, audio_file):
    tts = gTTS(text, lang='en')
    tts.save(audio_file)

def create_audio_for_prompts(prompts):
    for i, prompt in enumerate(prompts):
        content = generate_slide_content(prompt)
        generate_voiceover(content, f'voice_{i}.mp3')

prompts = [
    "Explain the importance of AI in modern technology.",
    "Describe how machine learning algorithms work.",
    "Summarize the key takeaways from AI advancements."
]

create_audio_for_prompts(prompts)



# Video Generation

from moviepy.editor import ImageSequenceClip, VideoFileClip, AudioFileClip

def create_video_from_images(image_folder, output_file, fps=1):
    image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith('.png')]
    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(output_file, codec="libx264")

def add_voiceover_to_video(video_file, audio_files, output_file):
    video = VideoFileClip(video_file)
    
    # Combine all audio files into a single audio track
    audio_clips = [AudioFileClip(audio_file) for audio_file in audio_files]
    final_audio = sum(audio_clips)
    
    video = video.set_audio(final_audio)
    video.write_videofile(output_file, codec="libx264")

# Assuming audio files are already generated in Part 1
audio_files = [f'voiceover_{i}.mp3' for i in range(len(prompts))]

# Execute Part 2
create_video_from_images('output_images', 'presentation_video.mp4')
add_voiceover_to_video('presentation_video.mp4', audio_files, 'final_presentation_video.mp4')
