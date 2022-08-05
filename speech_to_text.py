# Author: Endri Dibra

# Below i use the required libraries
import speech_recognition as sp

recognizer = sp.Recognizer()

while True:

    try:

        # Using the required method to use computer's microphone
        # to take user's speech from audio

        with sp.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic)

            # Converting my speech to text
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print("You said : ", text)

    except sp.UnknownValueError():

        # continues till an exception occurs
        recognizer = sp.Recognizer()

        continue
