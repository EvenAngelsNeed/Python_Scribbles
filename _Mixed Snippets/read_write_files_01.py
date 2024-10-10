
# -*- coding: utf-8 -*-
# python3
# read_write_files

import os



data = """
Some text.
----------
12356789abc
"""

file_write = 'test.txt'

with open(file_write, 'w+') as f:
   f.write(data);
   f.close



file_read = 'test.txt'

with open(file_read, 'r') as f:
   data = f.read();
   f.close



print("\nSaved Text to new file then reloaded it:\n")

print(data)

print("\n===== # =====\n")



# ======================

with open("file.bin", "wb") as f:
    data = b"\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x21" # Hello World! in Hex
    f.write(data)
    
    
with open("file.bin", "rb") as file:
    binary_data = file.read()

print("\nSaved Hex to new binary file then reloaded it:\n")

print(binary_data.decode())

print("\n===== # =====\n")




input()
