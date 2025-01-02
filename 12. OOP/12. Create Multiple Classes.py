class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print('Person Information')
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(30* '=')

class Staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print("Staff Information")
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

s1=Student("Ram",30)
s1.Details()

f1=Staff("Prof. Hema chandra",56)
f1.details()
