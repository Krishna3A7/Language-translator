import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# Creating Recogniser() class object
recog1 = spr.Recognizer()
mc = spr.Microphone()

# Function to capture voice and recognize text
def recognize_speech(recog, source):
    try:
        recog.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog.listen(source)
        recognized_text = recog.recognize_google(audio)
        return recognized_text
    except spr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except spr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Simulating frontend input for the target language
# In a real scenario, this input will come from the frontend
target_language_input = input("Enter the target language (e.g., 'Hindi', 'Telugu', 'Tamil'): ").strip()

# Mapping user input to language codes
language_map = {
    'Hindi': 'hi',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Tamil': 'ta',
    'Malayalam': 'ml',
    'Bengali': 'bn'
}

# Check if the target language is valid
if target_language_input not in language_map:
    print(f"Invalid language: {target_language_input}. Exiting.")
else:
    target_language_code = language_map[target_language_input]

    # Capture voice and directly translate
    with mc as source:
        print("Speak now for language detection and translation...")
        MyText = recognize_speech(recog1, source)

    # If the recognized text is valid, proceed with language detection and translation