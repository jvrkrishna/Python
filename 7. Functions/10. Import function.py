'''Import function
In python we can import and export the data.'''
# sample.py
def add(a,b):
    print(a+b)
    
def sub(a,b):
    print(a-b)

# anothersample.py
from Python.sample2 import add,sub
add(10,20)
