import os
from dotenv import load_dotenv
from elevenlabs import generate, play, set_api_key

load_dotenv()  # load .env configuration
api_key = os.getenv('ELEVEN_API_KEY')  # set API keys

set_api_key(api_key)  # specifically sets API key for elvenlabs API


def say(output_text):  # @input: str, output: bytes(stream) - performs text-to-speech operation on a given text
    try:
        audio = generate(
            text=output_text,
            voice="Gigi",
            model="eleven_multilingual_v1"
        )

        print(output_text)
        play(audio)

    except Exception as e:
        print("An error occured during speech synthesis: " + e)
