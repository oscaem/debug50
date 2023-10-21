import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)

load_dotenv()  # load .env configuration
api_key = os.getenv("OPENAI_API_KEY")  # set API keys

chat = ChatOpenAI(openai_api_key=api_key)  # configure chat object

messages = [
    SystemMessage(content="""
    You are helpful rubber duck debugger named Ducky. Quack, Quack. 
    You will help the user with rubber duck debugging. 
    You will not have access to the codebase, so try asking insightful questions.
    """)
]  # set up message structure and system prompt


def infer(input_text):  # @input: str, @output: str, - performs completion on a given text
    try:
        print("AI is thinking..")

        messages.append(HumanMessage(content=input_text))  # append Human Message to chat

        output_text = chat(messages=messages).content  # get response from AI
        messages.append(AIMessage(content=output_text))  # append AI Message to chat

        return output_text

    except Exception as e:
        print("An error occured during text completion: " + e)
