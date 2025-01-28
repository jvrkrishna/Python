######## File Handling #############
'''
File handling is an essential concept that allows you to read from and write to files. Python provides built-in functions to handle files in an easy and efficient way. 
'''

#Create a sample file sample1.py and create the below text
# Hello Welcome to python.

#Now do operations on demo.txt
#Example:
''' open   read   close'''
s=open('sample1.py',mode='r')
print(s.read())
s.close()

#Example:
''' open write close'''
s=open('sample1.py',mode='w')
s.write("Bye Bye")
s.close()

#Example
''' open append close'''
s=open('sample1.py',mode='a')
s.write("Bye Bye append")
s.close()

#Example:
''' open read and write close'''
s=open('sample1.py',mode='r+')
print(s.read())
s.write("r+ mode")
s.close()

#Example:
''' open write and read close'''
s=open('sample1.py',mode='w+')
print(s.tell()) #tell is used to know the current cursor pointer place
s.write("w+ mode")
print(s.tell())
s.seek(0) #seek is used to Move the file pointer to a specific position.
print(s.tell())
print(s.read())
s.close()

#Using with statement
'''In Python, it's a good practice to use the with statement when working with files. This ensures that the file is properly closed after its block is executed, even if an exception occurs.'''

#Example: Using with to read a file
# Using 'with' ensures the file is automatically closed
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
#Example: Using with to write to a file
with open('example.txt', 'w') as file:
    file.write("This is written using the 'with' statement.\n")
    file.write("It will automatically close the file when done.")

#Checking if a File Exists
#You might want to check if a file exists before opening it. You can use the os module for this:
import os

if os.path.exists('example.txt'):
    with open('example.txt', 'r') as file:
        print(file.read())
else:
    print("The file does not exist.")