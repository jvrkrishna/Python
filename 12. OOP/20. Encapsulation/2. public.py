#public
'''
==>Where we can access
    -with in the class
    -with in the child class
    -outside the class
'''

#Ex: Accessing variables
class A:
    def __init__(self):
        self.x=100 #public attribute
    
    def test(self):
        print(self.x) #We are accessing public attribute with in the class.
        
class B(A):
    def test1(self):
        print(self.x) #We are accessing public attribute with in the child class
        
a=A()
a.test()

b=B()
b.test1()

a=A()
print(a.x)#Accessing the public attribute outside the class

#Ex: Accessing Methods
class A:
    def m1(self): #public method
        print("m1 method")
    
    def test(self):
        self.m1() #we are calling public method inside the class

class B(A):
    def new_test(self):
        self.m1() #we are calling public method inside the child class.
        
a=A()
a.test()

b=B()
b.new_test()

a.m1()#we are calling public method outside of the class.