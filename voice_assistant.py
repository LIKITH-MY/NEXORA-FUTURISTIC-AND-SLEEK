# speak_text() and capture_voice()
import threading
import pyttsx3
import speech_recognition as sr

def speak_text(text):
    def _run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=_run, daemon=True).start()


def capture_voice():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        return r.recognize_google(audio), None

    except Exception as e:
        return None, str(e)
