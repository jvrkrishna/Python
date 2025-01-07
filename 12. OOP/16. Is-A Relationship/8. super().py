######## Super function ######
'''If parent class and child class having members with same name then from child class we can access parent class members using super().'''

#Without super():
'''Here we are creating same variables again and again like name and age.'''
class Student:
    def __init__(self,name,sid,age):
        self.name=name
        self.sid=sid
        self.age=age
    def details(self):
        print(f'Name is {self.name}')
        print(f'Student Id is {self.sid}')
        print(f'Age is {self.age}')
        
class Employee:
    def __init__(self,name,eid,age):
        self.name=name
        self.eid=eid
        self.age=age
    def details(self):
        print(f'Name is {self.name}')
        print(f'Employee Id is {self.eid}')
        print(f'Age is {self.age}')
s1=Student("rama","stu1",30)
s1.details()

#with super()
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        
class Employee(Person):
    def __init__(self,name,eid,age):
        super().__init__(name,age)
        self.eid=eid
    def details(self):
        super().details()
        print(f'Employee Id is {self.eid}')
        
class Student(Person):
    def __init__(self,name,sid,age):
        super().__init__(name,age)
        self.sid=sid
    def details(self):
        super().details()
        print(f'Student Id is {self.sid}')
        
e=Employee("Ram",1024,30)
e.details()

s=Student("Ram",101,30)
s.details()