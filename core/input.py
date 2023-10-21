import speech_recognition as sr


def listen():  # @input: none, @output: str - performs speech recognition (whisper) for a single cycle
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            audio = r.listen(source)  # catch audio stream from microphone
            input_text = r.recognize_whisper(audio, language="english", model="base")  # transcribe audio with model
            print("You said: ", input_text)
        return input_text

    except Exception as e:
        print("An error occured during input processing: " + e)
