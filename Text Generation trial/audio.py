import pandas as pd
from gtts import gTTS

def generate_audio(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file_path, encoding='latin1')
        except Exception as e:
            print(f"Error occurred while reading the CSV file: {e}")
            return

    if df.empty:
        print("Error: The CSV file is empty")
        return

    text_data = ' '.join(df.iloc[:, 0].astype(str).tolist())

    if not text_data.strip():
        print("The text data is empty.")
        return

    tts = gTTS(text_data)
    output_audio_file = 'Audio.mp3'
    tts.save(output_audio_file)

    print(f"Generated audio saved as {output_audio_file}")

generate_audio(r'D:\\Professional Mobility\\Text Generation trial\\text.csv')























































































# import pandas as pd
# from gtts import gTTS

# def generate_audio_from_csv(csv_file_path):
#     df = pd.read_csv(csv_file_path)
#     text_data = ' '.join(df.iloc[:, 0].astype(str).tolist())

#     tts = gTTS(text_data)
#     output_audio_file = 'output_audio.mp3'
#     tts.save(output_audio_file)

#     print(f"Generated audio saved as {output_audio_file}")

# generate_audio_from_csv('D:\\Professional Mobility\\Prof_mobility_challenge\\Tntra_Prof_Mob_Testcase_challenge.csv')




