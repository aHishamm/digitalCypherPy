import PySimpleGUI as sg
import digitalcypher
sg.theme('Purple')
layout = [  [sg.Text('Please enter the string to be encoded/decoded and the key: ')],
            [sg.InputText(k='-IN-')],
            [sg.InputText(k='-IN2-')],
            [sg.Button('Encode'), sg.Button('Decode'), sg.Button('Cancel')],
            [sg.Text('Converted DMS Coordinates', key='-OUTPUT-')],
            [sg.Input(key='-OUT')] 
            ]

window = sg.Window('Encrypter/Decrypter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	
        break
    if event == 'Encode':
        convertedVal = digitalcypher.encode(values['-IN-'],values['-IN2-'])
        print('You entered ', convertedVal)
        #window['-OUTPUT-'].update(convertedVal)
        window['-OUT'].update(convertedVal)
    if event == 'Decode':
        convertedVal = digitalcypher.decode(values['-IN-'],values['-IN2-'])
        print('You entered ', convertedVal)
        #window['-OUTPUT-'].update(convertedVal)
        window['-OUT'].update(convertedVal)
    
    if event == 'Go to Google Maps': 
        DMSConverter.GMapsRoute(convertedVal)

window.close()