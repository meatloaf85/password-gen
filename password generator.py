from random import choice
import PySimpleGUI as sg

characters = "abcdefghijklmnopqrstuvwrxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890!@$%^&*?~"
password = []
while len(password) < 14:
    n = choice(characters)
    password.append(n)
new_pass = "".join(password)


layout = [
            [sg.Text('Here is your password!'), sg.InputText(new_pass)],
            [sg.Button('Ok')]]


window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok':
        break

window.close()

