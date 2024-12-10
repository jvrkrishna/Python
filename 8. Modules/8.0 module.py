#Modules
'''In Python, a module is a file that contains Python code, such as functions, classes, variables, and runnable code.'''
#Requirement:
'''If we want to reuse the code then we go for function, but if we want to reuse group of variables, functions and classes in another file then we go for module.'''

#Types of Modules:
'''1.	Standard Modules or built in Modules
   2.	User Defined Modules
   3.	3rd party Modules'''

#1.	Standard Modules:
'''These modules is already available inside python software.
	Ex: os, sys, math etc'''
#Example:
import math
print(math.floor(2.14))
print(math.ceil(2.14))
print(math.factorial(5))

#2.	User defined Modules:
'''These Modules which is created by user as per requirement.
	Ex: sample, cal etc'''
#Example:
#sample1.py
def add(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)

#sample2.py
#Here we are importing add function from sample module
from Python.sample2 import add 
add(10,20)

#Here we are importing complete sample module i.e., all functions, variables all what ever
import Python.sample2 as sample2  
sample2.sub(10,20)

#3.	3rd party Modules:
'''These modules provided by 3rd party vendor, it is available on internet so we have to download it by using pip (i.e., pip install numpy) we cannot directly proceed with import.
	Ex: Numpy, pandas, matplotlib etc.'''

#Module Aliasing:
'''•	Giving another name to module is called module aliasing
        Ex: import sample as sam'''

#Module Member Aliasing:
'''•	Giving another name to module member is called module member aliasing.
        Ex: from sample import add as a, sub as s'''
