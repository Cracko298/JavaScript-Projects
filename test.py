Link = https://pypi.org/project/auto-py-to-exe/ #Link to convert .py to .exe
Link = https://realpython.com/pysimplegui-python/ #Link to Python Simple Gui
    

import os.path
import os
import tkinter
from tkinter import *

data_in_byte = b'\x64\x64'
def myClick1():
    message1 = Label(root, text="Health Set to 9999.")
    message1.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(33) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

root = Tk()
root.geometry("300x150")

myButton1 = Button(root, text="Click Me!", command=myClick1)
myButton1.pack()

root.mainloop()

#Edit Data in Bytes Code.
data_in_byte = b'\x64\x64' #Bytes to write to file
Data0 = "Data0" #Name of file

with open(Data0, 'rb+') as binary_file: #open file as binary
 binary_file.seek(33) #Move Editing to Offset 33
 binary_file.write(data_in_byte) #Writes the bytes from "data_in_byte"
