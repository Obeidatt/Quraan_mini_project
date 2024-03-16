import speech_recognition as sr

def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Record the entire audio file

        try:
            # Specify the language as Arabic (ar-AR)
            text = recognizer.recognize_google(audio_data, language="ar-AR")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")