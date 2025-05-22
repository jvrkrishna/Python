### Constructor Overloading ###
'''
Constructor overloading is a mechanism in which a class can have any number of constructors with different no of parameters of different type of parameters. Generally It doesnot support but we overcome with multi dispatch module.
'''

#Ex: Constructor Overloading which is not possible
class Test:
    def __init__(self,a):
        print(a)
    
    def __init__(self,a,b):
        print(a,b)
        
t=Test(10) #Gives Error -->Test.__init__() missing 1 required positional argument: 'b'


### How to archieve Constructor overloading in python by using variable length arguments.
class Test:
    def __init__(self,*a):
        print(a) 
t=Test(10)
t1=Test(10,20)


# Constructor overloading using multidispatch module
from multipledispatch import dispatch
class Test:
    @dispatch(int)
    def __init__(self,a):
        print(a)
    
    @dispatch(int,int)
    def __init__(self,a,b):
        print(a,b)
        
t=Test(10)
t1=Test(10,20)


