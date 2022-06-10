import webbrowser
import sys
import PySimpleGUI as sg

udemy = "https://www.udemy.com/"
linkedin = "https://www.linkedin.com/learning/"


#GUI Code

sg.theme('Dark Grey 6')  # window theme

layout = [
    [sg.Text("Which option would you like?")],
    [sg.Button("option1"), sg.Button("option2")]
]
window = sg.Window("Auto Web", layout, margins=(150,75))

#work begins

while True:
    event, values = window.read()
    #End program if user closes window or chooses a button
    if event == sg.WIN_CLOSED:
        break
    elif event == "option1":
        webbrowser.open_new(udemy) and webbrowser.open_new_tab(linkedin) and sys.exit()
    elif event == "option2":
        webbrowser.open_new(udemy) and webbrowser.open_new_tab(linkedin) and sys.exit()

window.close()