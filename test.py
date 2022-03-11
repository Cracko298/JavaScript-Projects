Link = https://pypi.org/project/auto-py-to-exe/ #Link to convert .py to .exe
Link = https://realpython.com/pysimplegui-python/ #Link to Python Simple Gui

import sys
import os
import PySimpleGUI as sg #Make sure to download this: pip install pysimplegui

#GUI Text Code
layout = [[sg.Text("9999 Health")], [sg.Button("Create")]]

#GUI Window Code
window = sg.Window(title="Ice Station Z Save Editor", layout=[[]], margins=(640, 960)).read()

#GUI Loop Code
while True:
    event, values = window.read()
    if event == ""Create" or event == sg.WIN_CLOSED:
        #Closes window if application is closed or the 9999 Health Button is pressed (Change)
        break #Exits Application

window.close() #Closes Window


#Edit Data in Bytes Code.
data_in_byte = b'\x0F\x27' #Bytes to write to file
Data0 = "Data0" #Name of file

with open(Data0, 'rb+') as binary_file: #open file as binary
 binary_file.seek(33) #Move Editing to Offset 33
 binary_file.write(data_in_byte) #Writes the bytes from "data_in_byte"
