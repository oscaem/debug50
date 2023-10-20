import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()  # load .env configuration
api_key = os.getenv("OPENAI_API_KEY")  # set API keys

llm = OpenAI(openai_api_key=api_key)  # assign language model


def infer(text):  # performs completion on a given text
    print("AI is thinking..")

    response = llm(text)
    return response
