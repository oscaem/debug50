import PySimpleGUI as sg
from gui.states import get_state, set_state

sg.theme('graygraygray')  # set theme for pysimplegui

font = ("Press Start 2P", 12)


img = sg.Image("gui/assets/duck.png", key='IMAGE')
btn = sg.Button("SPEAK", key='BUTTON', pad=(10, 10), border_width=0, size=(10, 1))

layout = [
    # [sg.Column([[sg.Text('DEBUG50', key='LABEL')]], justification='center')],
    [sg.Column([[img]], justification='center')],
    [sg.Column([[btn]], justification='center')],
]

window = sg.Window('', layout, font=font)  # initialize single window for pysimplegui


def update():
    state = get_state()

    # window['IMAGE'].update(state.value['image'])
    window['BUTTON'].update(state.value['text'])
    window.refresh()
