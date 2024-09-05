# Gemini API KEY == AIzaSyAaYr1XWQzOPSTKYOl0rMkLrNUXSNe3E4U        

sudo apt-get update -y
sudo apt-get install -y python3.11
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo update-alternatives --config python3
sudo apt-get install -y python3.11-distutils
wget https://bootstrap.pypa.io/get-pip.py
python3.11 get-pip.py

# !git clone https://github.com/SamurAIGPT/Text-To-Video-AI

# %cd Text-To-Video-AI

# !pip3.11 install -r requirements.txt


import os
os.environ["OPENAI_KEY"]="openai-key"
os.environ["PEXELS_KEY"]="pexels-key"

apt install imagemagick &> /dev/null
sed -i '/<policy domain="path" rights="none" pattern="@\*"/d' /etc/ImageMagick-6/policy.xml

python3.11 app.py "Beer"

from IPython.display import HTML
from base64 import b64encode

video_path = 'rendered_video.mp4'

def display_video(video_path, width=640, height=480):
    video_file = open(video_path, "rb").read()
    video_url = "data:video/mp4;base64," + b64encode(video_file).decode()
    return HTML(f"""
    <video width={width} height={height} controls>
        <source src="{video_url}" type="video/mp4">
    </video>
    """)

display_video(video_path)