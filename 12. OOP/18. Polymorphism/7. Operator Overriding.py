#### Operator Overriding #####
'''operator overriding (also called operator overloading) is possible in Python. This allows you to define how operators such as +, -, *, ==, and others behave when applied to instances of a custom class.

In Python, you can override operators by defining special methods in your class. These methods are often called "dunder" methods (short for "double underscore"), such as __add__, __sub__, __mul__, __eq__, and so on.

Examples of operator overriding:'''
#Ex: Operator Overriding without magic method (which is not possible)
class Employee:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,stipend):
        self.stipend=stipend

e=Employee(10000)
s=Student(5000)

#Now add Employee salary + Student Pocket Money
print(e+s) #Raises Error -- unsupported operand type(s) for +: 'Employee' and 'Student'

#Ex: Operator overriding with magic method
class Employee:
    def __init__(self,salary):
        self.salary=salary
    
    def __add__(self,other):  #We can use sub,gt,lt,ge,le etc.
        return self.salary+other.stipend

class Student:
    def __init__(self,stipend):
        self.stipend=stipend

e=Employee(10000)
s=Student(5000)

#Now add Emp salary + Stu Stipend
print(e+s) #Here if we use + then immediately checks for add magic method like this only remaining as well.