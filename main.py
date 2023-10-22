from core import dialogue
from ui.states import get_state
import ui.gui as gui


while True:
    event, values = gui.window.read()

    if event in (gui.sg.WIN_CLOSED, 'Quit'):
        break

    if event in ('BUTTON', 'Speak'):
        dialogue.talk()

    if event in ('Clear History'):
        dialogue.clear_history()

gui.window.close()
