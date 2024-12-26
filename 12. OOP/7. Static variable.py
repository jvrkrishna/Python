###Static variable
'''A variable that is shared across all instances of a class. It is class level variable.
If the value of variable is fixed to all objects then we can go for static variable.'''
class Person:
    school_name="Sri chaitanya" #static variable
    def Details(self,name,age):
        self.name=name #instance variable
        self.age=age   #instance variable

print(Person.school_name)    #We can call directly by class
p1=Person()
print(p1.school_name) #we can call by object as well
print(p1.__dict__)
print(Person.__dict__) # verify the static variable is class level object

'''
Creation of static variable in different places.
'''
#1. Inside the Class directly
class Person:
    school_name="Sri chaitanya" #static variable

print(Person.__dict__) #so it is class level variable thatsway we called with class
p1=Person()
print(p1.__dict__) #Here not works.

#2. Outside the Class 
class Person:
    pass
p1=Person()
Person.school_name="Sri Chaitanya" #static variable
print(Person.__dict__)

#3. Inside the constructor
class Person:
    def __init__(self):
        Person.school_name="Sri Chaitanya" #static variable

p1=Person()
print(Person.__dict__)

#4. Inside the Instance method
class Person:
    def Details(self):
        Person.school_name="Sri Chaitanya" #static variable

p1=Person()
p1.Details()
print(Person.__dict__)

#5. Inside class method by using class name
class Person:
    @classmethod
    def class_method(cls):  #here for class method 1st variable is "cls" like "self"
        Person.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
Person.class_method()
print(Person.__dict__)

#5.1 Inside class method by using cls variable
class Person:
    @classmethod
    def class_method(cls):
        cls.school_name="Sri Chaitanya"
        
Person.class_method()
print(Person.__dict__)

#6. Inside static method 
class Person:
    @staticmethod
    def static_method():  #here for static method 1st variable is nothing
        Person.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
Person.static_method()
print(Person.__dict__)