# import os

# def Speak(Text):
#     os.system(f"saly {Text}")
    

import pyttsx3

def Speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak the given text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Test the Speak function
# Speak("Hello, this is a test.")
