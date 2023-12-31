import PySimpleGUI as sg

sg.theme('graygraygray')  # set theme for pysimplegui

menu_layout = [
    ['Session',
     ['Speak', '---', 'Clear History', '---', 'Quit']
     ],
]  # menu bar setup

img = sg.Image(
    "ui/assets/duck.png", key='IMAGE'
)  # main image (duck)
btn = sg.Button(
    "SPEAK", key='BUTTON', pad=(10, 10), border_width=3, size=(10, 1),
)  # dialogue button (SPEAK)

layout = [
    [sg.Menu(menu_layout)],
    [sg.Column([[img]], justification='center')],
    [sg.Column([[btn]], justification='center')],
]  # PySimpleGUI window layout

window = sg.Window('', layout, finalize=True)  # initialize main window

