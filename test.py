Link = https://pypi.org/project/auto-py-to-exe/ #Link to convert .py to .exe


#Actual Code
import sys

data_in_byte = b'\x0F\x27'
Data0 = "Data0"

#Repl.it corrupts data files. Try on actual machine at later date
with open(Data0, 'rb+') as binary_file:
 binary_file.seek(33)
 binary_file.write(data_in_byte)
