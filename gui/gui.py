import PySimpleGUI as sg
from gui.states import get_state, set_state

sg.theme('graygraygray')  # set theme for pysimplegui

font = ("Press Start 2P", 12)

img = sg.Image("gui/assets/idle.png", key='IMAGE')
txt = sg.Text(key='TEXT', pad=(10, 2))
btn = sg.Button("Speak", key='SPEAK', pad=(10, 10), border_width=0, size=(8, 1))

layout = [
    [sg.Column([[img]], justification='center')],
    [sg.Column([[txt]])],
    [sg.Column([[btn]], justification='center')],
]

window = sg.Window('Mein Freund', layout, font=font)  # initialize single window for pysimplegui


def update():
    state = get_state()

    # window['IMAGE'].update(state.value['image'])
    window['TEXT'].update(state.value['text'])
    window.refresh()
