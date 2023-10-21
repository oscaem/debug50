from enum import Enum


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
