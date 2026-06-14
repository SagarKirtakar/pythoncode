"""
Description: File Handling
Author:      Sagar Kirtakar
Date:        2026-06-14
"""

"""
File Handling in Python
1) Open a file
2) read/write
3) close the file

File opening modes
r, w, a

r++, w++, a++

"""

print("Welcome to python Programming\n")

import os
def write_to_file(filename, name):
   # f = open(filename,"w")
   # f.write(name)
   # f.close()
   with open(filename, "w") as f:
      f.write(name)

def append_to_file(filename, name):
   f = open(filename,"a")
   f.write('\n')
   f.write(name)
   f.close()
   
def read_from_file(filename):
   try:
      f = open(filename, "r")
      text = f.read()
      print(text)
      f.close()
   except FileNotFoundError:
      print('File not found')
   

def main():
    name = input("Enter your name : ")
    write_to_file('file1.txt', name)
    #append_to_file('file1.txt',name)
    #read_from_file('file1.txt')
    #os.rename('file1.txt', 'file2.txt')
   #  try:
   #     os.remove('file2.txt')
   #  except FileNotFoundError:
   #    print('file not found')
main()   