import pyttsx3
from elevenlabs import generate, play, set_api_key

from config.settings import eleven_key
from ui.states import State, set_state


if eleven_key:  # confirm whether ELEVEN LABS key was provided, if not fallback to local solution
    set_api_key(eleven_key)
else:
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)


def generate_speech(text):
    if eleven_key:
        engine.say(text)
        engine.runAndWait()
    else:
        audio = generate(
            text=text,
            voice="Gigi",
            model="eleven_multilingual_v1"
        )
        play(audio)


def say(output_text):  # @input: str, output: bytes(stream) - performs text-to-speech operation on a given text
    try:
        set_state(State.SPEAK)
        print(output_text)
        generate_speech(output_text)
        set_state(State.IDLE)

    except Exception as e:
        print("An error occured during speech synthesis: " + str(e))
