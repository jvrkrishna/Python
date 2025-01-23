#protected
'''
==>Where we can access
    -with in the class
    -with in the child class
    -we cant access outside the class
    
note: _symbol used to create protected access modifier.
'''

#Ex: Accessing variables
class A:
    def __init__(self):
        self._x=100 #protected attribute
    
    def test(self):
        print(self._x) #we are accessing protected attributes with in the class

class B(A):
    def test1(self):
        print(self._x) #we are accessing protected attributes with in the child class

a=A()
a.test()

b=B()
b.test1()

a=A() 
print(a._x) #we are accessing protected outside of the class

#Note Python doesn't provide support for protected modifiers it is just a naming convention.

#Ex: Accessing Methods
class A:
    def _m1(self): #public method
        print("m1 method")
    
    def test(self):
        self._m1() #we are calling protected method inside the class

class B(A):
    def new_test(self):
        self._m1() #we are calling protected method inside the child class.
        
a=A()
a.test()

b=B()
b.new_test()

a._m1()#we are calling protected method outside of the class.

#Note Python doesn't provide support for protected modifiers it is just a naming convention.
