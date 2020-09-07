import PySimpleGUI as sg
import digitalcypher
import os 
sg.theme('Purple')
layout = [  [sg.Text('Please enter the string to be encoded/decoded and the key: ')],
            #[sg.InputText(k='-IN-')],
            #[sg.InputText(k='-IN2-')],
            [sg.Text('String', size=(8, 1)), sg.Input(k='-IN-'), sg.FileBrowse()],
            [sg.Text('Key',size=(8, 1)), sg.Input(k='-IN2-')],
            #[sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
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
        # add a conditional that checks the first letter of the string 
        # if the first letter of the string is / (basically a path)
        # then we'd access the file itself 
        if values['-IN-'][0] == '/' or values['-IN-'][0] == 'C:':
            f = open(values['-IN-'], 'r')
            #check if system is windows 
            if os.name == 'nt':
                writefile = open("C:/Users/cole1/Desktop/testering.txt",'w+')
            #change the write path to any other write path (only works with Linux)
            else:
                writefile = open("/home/abdulrahman/Desktop/test.txt",'w')
            fread = f.read()
            f.close()
            print(fread)
            convertedVal = digitalcypher.encode(fread,values['-IN2-'])
            print('You entered ', convertedVal)
            writefile.write(convertedVal)
            writefile.close()
            #window['-OUT'].update(convertedVal)
        #fix crash by writing the output of the if statement to a file instead of updating the window with it 
        #fixed 
        else:
            print('Original Value', values['-IN-'])
            convertedVal = digitalcypher.encode(values['-IN-'],values['-IN2-'])
            print('You entered ', convertedVal)
            #window['-OUTPUT-'].update(convertedVal)
            window['-OUT'].update(convertedVal)
    if event == 'Decode':
        convertedVal = digitalcypher.decode(values['-IN-'],values['-IN2-'])
        print('You entered ', convertedVal)
        #window['-OUTPUT-'].update(convertedVal)
        window['-OUT'].update(convertedVal)

window.close()