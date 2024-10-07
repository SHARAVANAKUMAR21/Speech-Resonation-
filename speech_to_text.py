import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        audio = recognizer.listen(source)

        try:
            spoken_text = recognizer.recognize_google(audio)
            return spoken_text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service."
