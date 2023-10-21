import os
from dotenv import load_dotenv


load_dotenv()  # load .env configuration

eleven_key = os.getenv('ELEVEN_API_KEY')
openai_key = os.getenv("OPENAI_API_KEY")  # set API keys