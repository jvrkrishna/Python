##### Constructor Overriding #####
'''Parent class constructor by default available to child class, If child class wont satisfy with parent class then child class can override it.'''
#Ex:
class Parent:
    def __init__(self):
        print('This is parent m1')
        
class Child(Parent):
    pass

c=Child()

#Ex:
class Parent:
    def __init__(self):
        print('This is parent m1')
        
class Child(Parent):
    def __init__(self):     #Constructor Overriding
        print('This is child m1')

c=Child()

#Ex problem without constructor overriding
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        
class Student():
    def __init__(self,name,age,course,college):
        self.name=name #Duplicate code
        self.age=age #Duplicate code
        self.course=course
        self.college=college
    
    def details(self):
        print(f"My name is {self.name}") #Duplicate code
        print(f"My age is {self.age}") #Duplicate code
        print(f"My COurse is {self.course}")
        print(f"My college is {self.college}")
        
class Employee():
    def __init__(self,name,age,dep,company):
        self.name=name #Duplicate code
        self.age=age #Duplicate code
        self.dep=dep
        self.company=company
    
    def details(self):
        print(f"My name is {self.name}") #Duplicate code
        print(f"My age is {self.age}") #Duplicate code
        print(f"My COurse is {self.dep}")
        print(f"My college is {self.company}")
        
e=Employee("Ram",30,"IT","Wipro")
e.details()

#Ex problem overcome with constructor overriding
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        
class Student(Human):
    def __init__(self,name,age,course,college):
        super().__init__(name,age)
        self.course=course
        self.college=college
    
    def details(self):
        super().details()
        print(f"My COurse is {self.course}")
        print(f"My college is {self.college}")
        
class Employee(Human):
    def __init__(self,name,age,dep,company):
        super().__init__(name,age)
        self.dep=dep
        self.company=company
    
    def details(self):
        super().details()
        print(f"My COurse is {self.dep}")
        print(f"My college is {self.company}")
        
e=Employee("Ram",30,"IT","Wipro")
e.details()