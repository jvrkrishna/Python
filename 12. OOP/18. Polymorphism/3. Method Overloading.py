###### Method Overloading ######
'''
-->If 2 or more methods have same name with different no of parameters of different type of parameters is called method overloading.
-->Python does not support method overloading. Other languages like java support it.
-->Because if we will define multiple methods then python will consider the last one only.
-->But indirectly we can archieve method overloading by using multiple dispatch decorator.
'''

#The advantages of method overloading
'''
->Code reusability.
->Provide flexibility and easy to programmer.
->It reduce complexity.
'''

#Ex:2 or more methods with same name but arguments are different.
class Test:
    def m1(self,a):
        print(a)
        
    def m1(self,a,b):
        print(a,b)
        
    def m1(self,a,b,c):
        print(a,b,c)
t=Test()
# t.m1(10)   #Gives Error-->Test.m1() missing 2 required positional arguments: 'b' and 'c'
#t.m1(10,20) #Gives Error-->Test.m1() missing 1 required positional argument: 'c'
t.m1(10,20,30) #Python takes latest updated method only in this cases.

### How to archieve method overloading in python by using variable length arguments.
class Test:
    def m1(self,*a):
        print(a)
t=Test()
t.m1(10)
t.m1(10,20,30)

### How to archieve method overloading by using multiple dispatch decorator.
#->pip install multipledispatch--> download this to use this module

#Method Overloading using multipledispatch module 
from multipledispatch import dispatch
class Test:
    @dispatch(int,int)
    def add(a,b):
        print(a+b)
    
    @dispatch(float,float)
    def add(a,b):
        print(a+b)
    
    @dispatch(int,float)
    def add(a,b):
        print(a+b)
    
    @dispatch(int,int,int)
    def add(a,b,c):
        print(a+b+c)
        
t=Test()
t.add(10,20)
t.add(40,13.4)
t.add(10,20,30)