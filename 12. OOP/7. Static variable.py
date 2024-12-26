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
