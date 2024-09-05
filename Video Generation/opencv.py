
import os
import win32com.client

def convert_ppt_to_images(ppt_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    powerpoint.Visible = True

    presentation = powerpoint.Presentations.Open(ppt_path, ReadOnly=True)

    for i, slide in enumerate(presentation.Slides):
        slide.Export(os.path.join(output_folder, f"slide_{i + 1}.png"), "PNG")

    presentation.Close()
    powerpoint.Quit()

ppt_path = r'D:\Professional Mobility\Video Generation\Machine Learning.pptx'
image_folder = r'D:\Professional Mobility\Video Generation\Image'
output_video = r'D:\Professional Mobility\Video Generation\cv2_video.mp4'

convert_ppt_to_images(ppt_path, image_folder)

import cv2

def create_video_from_images(image_folder, output_video, fps=1):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()

    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = first_image.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for img_name in images:
        img = cv2.imread(os.path.join(image_folder, img_name))
        video.write(img)

    video.release()
    print(f"Video saved as {output_video}")

# Create video from images
create_video_from_images(image_folder, output_video, fps=1)

