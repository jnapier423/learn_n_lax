import webbrowser
import sys
import PySimpleGUI as sg

udemy = "https://www.udemy.com/"
linkedin = "https://www.linkedin.com/learning/"
reddit = "https://reddit.com"
youtube = "https://youtube.com"
roll20 = "https://roll20.net"
twitch = "https://twitch.tv"

#GUI Code

sg.theme('Dark Grey 6')  # window theme

layout = [
    [sg.Text("Would you like to learn or relax?")],
    [sg.Button("Learn"), sg.Button("Relax")]
]
window = sg.Window("Auto Web", layout, margins=(150,75))

#work begins

while True:
    event, values = window.read()
    #End program if user closes window or chooses a button
    if event == sg.WIN_CLOSED:
        break
    elif event == "Learn":
        webbrowser.open_new(udemy) and webbrowser.open_new_tab(linkedin) and sys.exit()
    elif event == "Relax":
        webbrowser.open_new(reddit) and webbrowser.open_new_tab(youtube) and webbrowser.open_new_tab(roll20) and webbrowser.open_new_tab(twitch) and sys.exit()

window.close()