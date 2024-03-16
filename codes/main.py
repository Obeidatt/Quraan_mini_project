from speech_converter import speech_to_text  
import pandas as pd

df = pd.read_csv("quraan.csv")

def tester(audiofile):
    result = speech_to_text(audiofile)
    return df[df["Ayah_text"].str.contains(result)]


#Main Code:
audio_file_path1 = "ayah.wav"
audio_file_path2 = "test2.wav"
print(tester(audio_file_path1))
print(100*'-')
print(tester(audio_file_path2))


FutureWarning