#private
'''
==>Where we can access
    -with in the class
    -we cant access inside the child class
    -we cant access outside the class
    
note: __symbol used to create private access modifier.
'''

#Ex: Accessing variable inside the class
class A:
    def __init__(self):
        self.__x=100 #private attribute
    
    def test(self):
        print(self.__x) #We are accessing private attribute with in the class.
        
        
a=A()
a.test()

#Ex: Accessing variable inside the child class
class A:
    def __init__(self):
        self.__x=100 #private attribute
    
class B(A):
    def test(self):
        print(self.__x) #we cannot access private attribute inside the class raise error
             
b=B()
b.test()

#Ex: Accessing variable outside the class
class A:
    def __init__(self):
        self.__x=100 #private attribute
             
a=A()
print(a.__x)#we cannot access private attribute outside the class raise error

#Ex: Accessing Methods inside the class
class A:
    def _m1(self): #private method
        print("m1 method")
    
    def test(self):
        self._m1() #we are calling private method inside the class

# class B(A):
#     def new_test(self):
#         self._m1() #we are calling private method inside the child class.
        
a=A()
a.test()

#Ex: Accessing Methods inside the child class
class A:
    def _m1(self): #private method
        print("m1 method")

class B(A):
    def new_test(self):
        self._m1() #we are calling private method inside the child class which is not possible.

b=B()
b.new_test()

#Ex: Accessing Methods outside the child class
class A:
    def _m1(self): #private method
        print("m1 method")

a=A()
a.__m1() #we are calling private method outside the class which is not possible.