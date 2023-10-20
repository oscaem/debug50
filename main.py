import gui.gui as gui, input.input as input, inference.inference as inference, output.output as output
# handles: gui, input, inference, output
from gui.states import set_state, State


while True:
    event, values = gui.window.read(timeout=100)

    gui.update()

    if event == gui.sg.WIN_CLOSED:
        break

    if event == 'SPEAK':
        set_state(State.LISTEN)
        gui.update()
        text = input.listen()
        set_state(State.THINK)
        gui.update()
        response = inference.infer(text)
        set_state(State.SPEAK)
        gui.update()
        output.say(response)
        set_state(State.IDLE)
        gui.update()

gui.window.close()
