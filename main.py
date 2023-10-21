import gui.gui as gui
import input.input as input
import inference.inference as inference
import output.output as output

from gui.states import set_state, State


def update_state(state):
    set_state(state)
    gui.update()


def perform_dialogue():
    update_state(State.LISTEN)
    text = input.listen()  # listen for and transcribe voice input

    update_state(State.THINK)
    response = inference.infer(text)  # infer answer from text input

    update_state(State.SPEAK)
    output.say(response)  # synthesize voice output

    update_state(State.IDLE)  # reset state to origin


while True:
    event, values = gui.window.read(timeout=100)

    gui.update()

    if event == gui.sg.WIN_CLOSED:
        break

    if event == 'BUTTON':
        perform_dialogue()

gui.window.close()
