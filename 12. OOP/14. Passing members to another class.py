###Passing one class members to another class 
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @staticmethod
    def modify(x): #### x is object reference where s1 and x are same.
        x.age=31 
              
s1=Student("Ram",30)
s1.Details()

Staff.modify(s1)  #Here we are passing complete object (s1 ---- x)
s1.Details()

###Here we are passing only one object from one class to another class
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @staticmethod
    def modify_age(x): 
        print(x) 

s1=Student("Ram",30)
Staff.modify_age(s1.age)  #Here s1 has two objects but we are taking only age in to x.
