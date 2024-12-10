#interacting with the operating system, providing access to the underlaying of the operating system.

import os
print(os.getcwd())  #current working directory

print(os.listdir())  #list of dir in current directory

#change directory
print(os.chdir(r"E:\Python Full Stack\last\TUTORIALS\New folder"))
print(os.getcwd())  #current working directory