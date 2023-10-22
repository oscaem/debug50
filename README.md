# CS50 Final Project: Rubber Duck Debugger

Hello there and welcome to my final project for CS50 Computer Science 2023 course! This project is a GUI application that is inspired by the concept of 'Rubber Duck Debugging'. If you have ever tried to explain your code to an inanimate object and found that the solution magically unfolded itself, you know exactly what I'm talking about. It was also inspired by CS50's very own duck debugger, integrated into their codespace. 

The application aims to make the process of debugging a bit more enjoyable and interactive, by providing you with an AI-powered rubber duck! You can talk to the duck about your code and the AI will attempt to provide you with debugging suggestions. The whole experience is designed to be immersive and engaging, hopefully making those tough debugging sessions a bit more bearable.

Video Demo: https://youtu.be/Qafp-aZ0LE0

<img width="949" alt="Bildschirmfoto 2023-10-22 um 12 52 44" src="https://github.com/oscaem/debug50/assets/48035650/3e038ac3-3539-4604-b7f8-1240e1e623d7">


# How it Works
The GUI is built with PySimpleGUI library. When you interact with the application by clicking the "Speak" button, a chain of processes gets initiated. Here's the flow:

- **Speech Recognition:**
  - The app accesses your computer's local microphone and tries to recognize your spoken input using the `openai-whisper` library and `pyaudio`.
  - The spoken input is then transcribed into text using a Speech to text model.

- **Text Inference:**
  - The transcript is processed by the `text_inference` component.
  - This component makes use of the `langchain` library to compose an array of messages which includes the entire dialogue between you and the rubber duck.
  - The messages are then sent to the OpenAI server for text inference.

- **Speech Synthesis:**
  - The AI-generated response is converted back to speech using either the `py3-tts` or `elevenlabs` models depending on the availability of the latter.
  - The speech is then played back to you, creating an illusion of a real dialogue with the rubber duck.

This entire dialogue chain and the AI's debugging capabilities have been tailored for the purpose of rubber duck debugging. The duck's voice output, dialogue style and other features are opinionated to make the debugging session as pleasant as it can be.

# Future Improvements
Some additional features that could be incorporated to enhance the current application are:
- Keyboard shortcuts for different operations.
- Option to show transcripts and chat in text.
- Settings to change language, volume, and so on. 
For now, they have not been included due to the scope of this project. But who knows what the future holds!

# Installation
To start using the software, you'll need to:

1. Clone the repository.
2. pip install all the required external libraries from `pip install -r requirements.txt`.
3. Create a `.env` file with your OpenAI_API_KEY which is a requirement. You can find more information on this here: https://platform.openai.com/docs/quickstart.
4. Optionally, you can also provide an `ELEVEN_API_KEY` from elevenlabs.io, a text-to-speech provider. More information on this can be found here: https://docs.elevenlabs.io/api-reference/quick-start/introduction.

# Conclusion
To wrap up, I hope you enjoy the application and find it to be a handy tool while debugging your code. Through the journey of creating this project, I learned a lot about speech synthesis, language models, dialogue engineering, and more. It was a fun way to explore these areas and I hope you'll have an equally fun time using it. Happy Debugging, everyone!
