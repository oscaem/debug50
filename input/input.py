import speech_recognition as sr


def listen():  # @input: none, @output: str - performs speech recognition (whisper) for a single cycle
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)  # catch audio stream from microphone
        text = r.recognize_whisper(audio, language="english", model="base")  # transcribe audio with model
        print("You said: ", text)
    return text

