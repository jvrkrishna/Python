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


###Accessing static variable in different places
#1. Outside the class
class Person:
    school_name="Sri Chaitanya"

print(Person.school_name)

#2. Inside the constructor
class Person:
    school_name="Sri Chaitanya"
    
    def __init__(self):
        print(Person.school_name)

p1=Person()

#3. Inside the Instance method
class Person:
    school_name="Sri Chaitanya"
    
    def details(self):
        print(Person.school_name)

p1=Person()
p1.details()

#4. Inside class method
class Person:
    school_name="Sri Chaitanya"
    @classmethod
    def class_method(cls):
        print(Person.school_name)
        
Person.class_method()

#5. Inside static Method
class Person:
    school_name="Sri Chaitanya"
    @staticmethod
    def static_method():
        print(Person.school_name)
        
Person.static_method()

###Modifying static  variable in different places
#1. Outside of the class
class Person:
    school_name="Sri Chaitanya"
        
print(Person.school_name)
Person.school_name="Mod Sri Chaitanya"
print(Person.school_name)

#2. Inside the constructor
class Person:
    school_name="Sri Chaitanya"
    def __init__(self):
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
print(Person.school_name)

#3. Inside instance method
class Person:
    school_name="Sri Chaitanya"
    def details(self):
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
p1.details()
print(Person.school_name)

#4. Inside class method
class Person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def class_method(cls):
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
p1.class_method()
print(Person.school_name)

#5. Inside static method
class Person:
    school_name="Sri Chaitanya"
    
    @staticmethod
    def static_method():
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
p1.static_method()
print(Person.school_name)

###Deletion static variable in different places
#1. Outside the class
class Person:
    school_name="Sri Chaitanya"
        
print(Person.__dict__)

del Person.school_name
print(Person.__dict__)

#2. Inside the class
class Person:
    school_name="Sri Chaitanya"
    del school_name
        
print(Person.__dict__)

#3. Inside the Constructor
class Person:
    school_name="Sri Chaitanya"
    def __init__(self):
        del Person.school_name
        
print(Person.__dict__)

p1=Person()
print(Person.__dict__)

#4. Inside the instance method
class Person:
    school_name="Sri Chaitanya"
    def details(self):
        del Person.school_name
        
print(Person.__dict__)

p1=Person()
p1.details()
print(Person.__dict__)

#5. Inside the class method
class Person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def class_method(cls):
        del Person.school_name
        
print(Person.__dict__)
Person.class_method()
print(Person.__dict__)

#6. Inside the static method
class Person:
    school_name="Sri Chaitanya"
    
    @staticmethod
    def static_method():
        del Person.school_name
        
print(Person.__dict__)
Person.static_method()
print(Person.__dict__)


