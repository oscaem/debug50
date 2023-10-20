import PySimpleGUI as sg
from gui.states import get_state, set_state

sg.theme('graygraygray')  # set theme for pysimplegui

font = ("Press Start 2P", 12)

layout = [
    [sg.Image("gui/assets/idle.png", key='IMAGE')],
    [sg.Text(key='TEXT')],
    [sg.Button("Speak", key='SPEAK')]
]

window = sg.Window('Mein Freund', layout, font=font)  # initialize single window for pysimplegui


def update():
    state = get_state()

    # window['IMAGE'].update(state.value['image'])
    window['TEXT'].update(state.value['text'])
    window.refresh()
