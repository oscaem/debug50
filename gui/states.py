from enum import Enum


class State(Enum):
    IDLE = {'image': './gui/assets/idle.png', 'text': 'Waiting..'}
    LISTEN = {'image': './gui/assets/listen.png', 'text': 'Listening..'}
    THINK = {'image': './gui/assets/think.png', 'text': 'Thinking..'}
    SPEAK = {'image': './gui/assets/speak.png', 'text': 'Speaking..'}


current_state = State.IDLE  # initialize State to IDLE


def get_state():
    return current_state


def set_state(new_state):
    global current_state
    current_state = new_state
