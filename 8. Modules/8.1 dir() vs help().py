#dir() function will give only the members

#help() function will give all the member name along with description.
# import math
# print(dir(math))
# print(help(math))

#Example:
#sample1.py
a=10
b=20
def add(a,b):
    print(a+b)

#sample2.py
import sample1 
print(help(sample1))

#help output:
'''Help on module sample1:

NAME
    sample1

FUNCTIONS
    add(a, b)

DATA
    a = 10
    b = 20

FILE
    c:\users\jvrkr\git-repo\python\sample1.py


None'''

#sample2.py
import sample1 
print(dir(sample1))

#dir output:
'''['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'add', 'b']'''