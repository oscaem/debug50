import speech_recognition as sr


def listen():  # performs speech recognition (whisper) for a single cycle
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
        text = r.recognize_whisper(audio, language="german", model="base")
        print("You said: ", text)
    return text
