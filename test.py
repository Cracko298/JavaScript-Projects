Link = https://pypi.org/project/auto-py-to-exe/ #Link to convert .py to .exe
Link = https://realpython.com/pysimplegui-python/ #Link to Python Simple Gui
    

import os.path
import os
import tkinter
from tkinter import *

data_in_byte = b'\x64\x64'
def myClick1():
    message1 = Label(root, text="Data0 (Slot 1): Health Was Set To 9999.")
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

data_in_byte = b'\x64\x64'
def myClick2():
    message2 = Label(root, text="Data0 (Slot 1): Food Was Set To 9999.")
    message2.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(36) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick3():
    message3 = Label(root, text="Data0 (Slot 1): Battery Was Set To 9999.")
    message3.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(39) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick4():
    message2 = Label(root, text="Data0 (Slot 1): Water Was Set To 9999.")
    message2.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data0 = "Data0" 
    #Name of file

    with open(Data0, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(42) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"
#======================================================================================================#

data_in_byte = b'\x64\x64'
def myClick5():
    message1 = Label(root, text="Data1 (Slot 2): Health Was Set To 9999.")
    message1.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(33) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick6():
    message2 = Label(root, text="Data1 (Slot 2): Food Was Set To 9999.")
    message2.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(36) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick7():
    message3 = Label(root, text="Data1 (Slot 2): Battery Was Set To 9999.")
    message3.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(39) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

data_in_byte = b'\x64\x64'
def myClick8():
    message2 = Label(root, text="Data1 (Slot 2): Water Was Set To 9999.")
    message2.pack()
    #Edit Data in Bytes Code.
    data_in_byte = b'\x64\x64' 
    #Bytes to write to file
    Data1 = "Data1" 
    #Name of file

    with open(Data1, 'rb+') as binary_file:
      #open file as binary
      binary_file.seek(42) 
      #Move Editing to Offset 33
      binary_file.write(data_in_byte) 
      #Writes the bytes from "data_in_byte"

root = Tk()
root.geometry("750x450")

myButton1 = Button(root, text="Data0 (Slot 1): 9999 Health", command=myClick1, fg="white", bg="black")
myButton1.pack()

myButton2 = Button(root, text="Data0 (Slot 1): 9999 Food", command=myClick2, fg="white", bg="black")
myButton2.pack()

myButton3 = Button(root, text="Data0 (Slot 1): 9999 Battery", command=myClick3, fg="white", bg="black")
myButton3.pack()

myButton4 = Button(root, text="Data0 (Slot 1): 9999 Water", command=myClick4, fg="white", bg="black")
myButton4.pack()

myButton5 = Button(root, text="Data1 (Slot 2): 9999 Health", command=myClick5, fg="black", bg="white")
myButton5.pack()

myButton6 = Button(root, text="Data1 (Slot 2): 9999 Food", command=myClick6, fg="black", bg="white")
myButton6.pack()

myButton7 = Button(root, text="Data1 (Slot 2): 9999 Battery", command=myClick7, fg="black", bg="white")
myButton7.pack()

myButton8 = Button(root, text="Data1 (Slot 2): 9999 Water", command=myClick8, fg="black", bg="white")
myButton8.pack()

root = Tk()
root.geometry("750x450")

root.mainloop()

#Edit Data in Bytes Code.
data_in_byte = b'\x64\x64' #Bytes to write to file
Data0 = "Data0" #Name of file

with open(Data0, 'rb+') as binary_file: #open file as binary
 binary_file.seek(33) #Move Editing to Offset 33
 binary_file.write(data_in_byte) #Writes the bytes from "data_in_byte"
