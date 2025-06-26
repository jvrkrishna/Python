###Static variable
'''A variable that is shared across all instances of a class. It is class level variable.
If the value of variable is fixed to all objects then we can go for static variable.'''

#########Creation of static variable#########
#Example 1: Creation of static variable inside the Class
class Person:
    school_name="Sri chaitanya" #static variable

print(Person.school_name)    #We can call directly by class
p1=Person()
print(p1.school_name) #We can call by object as well
print(Person.__dict__)  # verify the static variable is class level object
print(p1.__dict__)   #Static variable is not object level 

#Example 2: Creation of static variable outside the Class
class Person:
    pass
p1=Person()
Person.school_name="Sri Chaitanya" #static variable
print(Person.__dict__)

p1.school_name="Sri Chaintanya"
print(p1.__dict__)


#Example 3: Creation of static variable inside the constructor
class Person:
    def __init__(self):
        Person.school_name="Sri Chaitanya" #static variable

p1=Person()
print(Person.__dict__)

#Example 4: Creation of static variable inside the Instance method
class Person:
    def Details(self):
        Person.school_name="Sri Chaitanya" #static variable

p1=Person()
p1.Details()
print(Person.__dict__)

#Example 5: Creation of static variable inside the class method by using class name
class Person:
    @classmethod
    def class_method(cls):  #here for class method 1st variable is "cls" like "self"
        Person.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
Person.class_method()
print(Person.__dict__)

#Example 5.1: Creation of static variable inside the class method by using cls variable
class Person:
    @classmethod
    def class_method(cls):
        cls.school_name="Sri Chaitanya"
        
Person.class_method()
print(Person.__dict__)

#Example 6: Creation of static variable inside the static method by using class name
class Person:
    @staticmethod
    def static_method():  #here for static method 1st variable is nothing
        Person.school_name="Sri Chaitanya" #static variable
        
#Here in this case no need to create object we directly call class methods with class name reference.
Person.static_method()
print(Person.__dict__)


###########Accessing the static variable###########
#Example 1: Accessing the static variable outside the class
class Person:
    school_name="Sri Chaitanya"

print(Person.school_name)

#Example 2: Accessing the static variable inside the constructor
class Person:
    school_name="Sri Chaitanya"
    
    def __init__(self):
        print(Person.school_name)

p1=Person()

#Example 3: Accessing the static variable inside the Instance method
class Person:
    school_name="Sri Chaitanya"
    
    def details(self):
        print(Person.school_name)

p1=Person()
p1.details()

#Example 4: Accessing the static variable inside the class method
class Person:
    school_name="Sri Chaitanya"
    @classmethod
    def class_method(cls):
        print(Person.school_name)
        
Person.class_method()

#Example 5: Accessing the static variable inside the static method
class Person:
    school_name="Sri Chaitanya"
    @staticmethod
    def static_method():
        print(Person.school_name)
        
Person.static_method()

######### Modify static variable ############
#Example 1: Modify the static variable outside the class
class Person:
    school_name="Sri Chaitanya"
        
print(Person.school_name)
Person.school_name="Mod Sri Chaitanya"
print(Person.school_name)

#Example 2: Modify the static variable inside the class and inside the constructor
class Person:
    school_name="Sri Chaitanya"
    def __init__(self):
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
print(Person.school_name)

#Example 3: Modify the static variable inside the class and inside the instance method
class Person:
    school_name="Sri Chaitanya"
    def details(self):
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
p1.details()
print(Person.school_name)

#Example 4: Modify the static variable inside the class and inside the class method
class Person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def class_method(cls):
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
p1.class_method()
print(Person.school_name)

#Example 5: Modify the static variable inside the class and inside the static method
class Person:
    school_name="Sri Chaitanya"
    
    @staticmethod
    def static_method():
        Person.school_name="Mod Sri Chaitanya"
        
print(Person.school_name)
p1=Person()
p1.static_method()
print(Person.school_name)

########### Deletion of static variable #############
#Example 1: Deletion of static variable outside the class
class Person:
    school_name="Sri Chaitanya"
        
print(Person.__dict__)

del Person.school_name
print(Person.__dict__)

#Example 2: Deletion of static variable Inside the class
class Person:
    school_name="Sri Chaitanya"
    del school_name
        
print(Person.__dict__)

#Example 3: Deletion of static variable inside the class and inside the constructor
class Person:
    school_name="Sri Chaitanya"
    def __init__(self):
        del Person.school_name
        
print(Person.__dict__)

p1=Person()
print(Person.__dict__)

#Example 4: Deletion of static variable inside the class and inside the instance method
class Person:
    school_name="Sri Chaitanya"
    def details(self):
        del Person.school_name
        
print(Person.__dict__)

p1=Person()
p1.details()
print(Person.__dict__)

#Example 5: Deletion of static variable inside the class and inside the class method
class Person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def class_method(cls):
        del Person.school_name
        
print(Person.__dict__)
Person.class_method()
print(Person.__dict__)

#Example 6: Deletion of static variable inside the class and inside the static method
class Person:
    school_name="Sri Chaitanya"
    
    @staticmethod
    def static_method():
        del Person.school_name
        
print(Person.__dict__)
Person.static_method()
print(Person.__dict__)


