###Passing one class members to another class using Instance method
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    def modify(self,x): #### x is object reference where s1 and x are same.
        x.age=31
              
s1=Student("Ram",30)
s1.Details()

s2=Staff()
s2.modify(s1)
s1.Details()

###Here we are passing only one object from one class to another class using instance method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    def modify_age(self, x):  # instance method (requires self)
        print(f'Modified Age: {x}')

s1 = Student("Ram", 30)
staff1 = Staff()  # creating an instance of Staff
staff1.modify_age(s1.age)  # calling instance method with self

###Passing one class members to another class using Class method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @classmethod
    def modify_student(cls, student_obj):  # class method
        student_obj.age = 31
        print("Student age modified by class method in Staff")

s1 = Student("Ram", 30)
s1.Details()

Staff.modify_student(s1)  # class method can be called from class
s1.Details()

###Here we are passing only one object from one class to another class using class method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Details(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')

class Staff:
    @classmethod
    def modify_age(cls, x):  # class method (uses cls)
        print(f'Modified Age: {x}')

s1 = Student("Ram", 30)
Staff.modify_age(s1.age)  # works like static method, but passes class as first arg

###Passing one class members to another class  using static method
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

###Here we are passing only one object from one class to another class using static method
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
