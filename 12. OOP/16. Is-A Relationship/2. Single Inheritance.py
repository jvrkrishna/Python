#Single Inheritance
'''
. In single inheritance a one child class is derived from one parent class.

class A ------> class B(A)

. Child class can access parent class members as well as own members.

. But the parent class only can access its own members it can't access the members of the child class.
'''
#Example:
class A: #parent class
    def method1(self):
        self.x=10
        self.y=20
        print(f"value of x is {self.x}")
    def method2(self):
        self.z=30
        print(f"value of z is {self.z}")
class B(A):
    pass        

b=B()
b.method1()
b.method2()

#Example: Parent class can only access of there own properties but child class can access both parent and its own properties.
class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class method2")
class B(A):
    def method3(self):
        print("B class method3")
a=A()
a.method1()
a.method2()

b=B()
b.method3()
b.method1()
b.method2()

#Example: child class can access constructor, instance method, staticmethod, classmethod.
class A:
    a=10
    print(f"value of a is {a}")
    
    def __init__(self):
        self.b=15
        print(f"value of b is {self.b}")
    
    def method1(self):
        y=20
        self.x=30
        print(f"value of x is {self.x}")
        print(f"value of y is {y}")
        
    @classmethod
    def cm(cls):
        cls.cmv=40
        print(f"value of cmv is {cls.cmv}")
        
    @staticmethod
    def sm():
        smv=50
        print(f"value of smv is {smv}")
        
class B(A):
    pass        

b=B()
b.method1()
b.cm()
b.sm()

