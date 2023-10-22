import speech_recognition as sr

from ui.states import State, update_state


def listen():  # performs speech recognition (whisper) for a single cycle
    try:
        update_state(State.LISTEN)  # set corresponding State flag for action

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            audio = r.listen(source)  # catch audio stream from microphone
            input_text = r.recognize_whisper(audio, language="english", model="base")  # transcribe audio with model
            print("You said: ", input_text)
            return input_text

    except Exception as e:
        print("An error occured during input processing: " + str(e))
