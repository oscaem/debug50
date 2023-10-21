from core import text_inference, voice_input, voice_output


def talk():  # main dialogue chain, optionally pass a gui object

    text = voice_input.listen()  # listen for and transcribe voice input

    if text:
        response = text_inference.respond(text)  # infer answer from text input
        voice_output.say(response)  # synthesize voice output


def clear_history():  # clear the chat history, resetting memory of AI
    text_inference.clear()