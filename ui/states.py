from enum import Enum
from ui import gui


class State(Enum):
    IDLE = {'image': '', 'text': 'SPEAK'}
    LISTEN = {'image': '', 'text': 'LISTENING..'}
    THINK = {'image': '', 'text': 'THINKING..'}
    SPEAK = {'image': '', 'text': 'SPEAKING..'}


current_state = State.IDLE  # initialize State to IDLE


def get_state():
    return current_state


def set_state(new_state):
    global current_state
    current_state = new_state
    return current_state


def update_state(state):
    new_state = set_state(state)
    gui.window['BUTTON'].update(new_state.value['text'])
    gui.window.refresh()
    print(get_state())
