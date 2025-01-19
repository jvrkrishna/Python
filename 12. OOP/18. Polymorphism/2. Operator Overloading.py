######## Operator Overloading #######
'''
-->If we will use same operator in different purposes then it is called operator overloading.
-->we are using +, * and etc in operator for different purposes.
-->Python supports operator overloading other languages like java does not support it.
-->we will use corresponding magic method to overload operator.
'''
#Ex:
print(10+20)
print('Ram'+'Krishna')
'''In the above example operator work in different formats like adding, concatination'''

#Ex: Operator overloading without magic method (which is not possible)
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

#Ex: Operator overloading with magic method
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
