#1. IS-A Relationship / Inheritance
'''
Inheritance is a mechanism for creating a new class from an existing class.
Here the old class is called Base class and the new class is called Derived class.
'''

#Example:
'''
class A -->Old class/ Base Class/ Parent Class
  ..
  ..
  ..
  ..
  ..
class B(A) -->New Class/ Derived Class/ Child Class/ Sub Class/ Extended Class.
'''

#Example:
'''
            Person
            *    *
     IS-A  *      * IS-A
          *        *
         *          *
    Employee        Student
    
In the above 
    Employee IS-A Person.
    Student IS-A Person           
'''

#Example:
class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class method2")
class B:
    def method3(self):
        print("B class method3")

b=B()
b.method3()
b.method1() #Here B object has no attribute 'method1'

#Example:
class A:
    def method1(self):
        print("A class Method1")
    def method2(self):
        print("A class method2")
class B(A):    #Here B extends a
    def method3(self):
        print("B class method3")

b=B()
b.method3()
b.method1() #Here it works

'''
B class method3
A class Method1
'''

#Example:
class A:
    def __init__(self):
        self.x=10
        self.y=20
        
class B(A):
    def Details(self):
        print(f'x is {self.x}')
        print(f'y is {self.y}')
b=B()
b.Details()

'''
x is 10
y is 20
'''

#Example: Without Inheritance
class A:
    def __init__(self):
        self.x=10
        self.y=20
        
class B:
    def __init__(self):  #Here without Inheritance code usabilty is repeated
        self.x=10
        self.y=20
    def Details(self):
        print(f'x is {self.x}')
        print(f'y is {self.y}')
        
b=B()
b.Details()

'''
x is 10
y is 20
'''

#Adv and Disadv of Inheritance
'''
Adv:
1. Code reusability.
2. Reduce the code.
3. Code extensibility(By overriding the base class functionality).

DisAdv:
1. Base and derived class both are tightly coupled(If we made any changes on parent class it will directly reflect on child class).
'''

#Example about Disadvantage: If we change the value in parent class it will reflect in child class that's way Inheritance concept is tightly coupled.
class A:
    def m1(self):
        self.x=10 #If we change the value it will reflect every were
        print(f"Value or x is {self.x}")

class B(A):
    pass

b=B()
b.m1()

#Example: If we change the value in child class it will not reflect in parent class.
class A:
    def m1(self):
        self.x=10
        print(f"Value or x is {self.x}")

class B(A):
    def m2(self):
        self.x=20
        

b=B()
b.m1()
        
        