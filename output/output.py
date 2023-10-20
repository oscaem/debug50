import os
from dotenv import load_dotenv
from elevenlabs import generate, play, set_api_key

load_dotenv()  # load .env configuration
api_key = os.getenv('ELEVEN_API_KEY')  # set API keys

set_api_key(api_key)  # specifically sets API key for elvenlabs API


def say(text):  # performs text-to-speech operation on a given text
    audio = generate(
        text=text,
        voice="Gigi",
        model="eleven_multilingual_v1"
    )

    print(text)
    play(audio)
