import speech_recognition as sr

from ui.states import State, set_state


def listen():  # performs speech recognition (whisper) for a single cycle
    try:
        set_state(State.LISTEN)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            audio = r.listen(source)  # catch audio stream from microphone
            input_text = r.recognize_whisper(audio, language="english", model="base")  # transcribe audio with model
            print("You said: ", input_text)
            return input_text

    except Exception as e:
        print("An error occured during input processing: " + str(e))
