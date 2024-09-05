from pptx import Presentation
from PIL import Image
from moviepy.editor import ImageClip, concatenate_videoclips
import io
import numpy as np

def extract_slide_as_image(slide):
    img = Image.new('RGB', (1280, 720), color=(73, 109, 137))
    return img

prs = Presentation('D:\\Professional Mobility\\Video Generation\\Unit 1.pptx')

slides = []
for slide in prs.slides:
    slide_image = extract_slide_as_image(slide)  
    np_image = np.array(slide_image) 
    clip = ImageClip(np_image).set_duration(5)  
    slides.append(clip)

video = concatenate_videoclips(slides)

video.write_videofile('output_video.mp4', fps=24)
