##########Instance variable####################
'''
Instance variables are variables that belong to a specific instance (object) of a class.
'''

#Example:
class Person:
    def __init__(self,name,age):
        self.name=name #instance variable
        self.age=age   #instance variable
        
p1=Person("Ram",30)   #p1 is one instance
p2=Person("gopal",25) #p2 is one instance

print(p1.__dict__)
print(p2.__dict__)

#Example:
class Person:
    school_name="Sri chaitanya"
    def Details(self,name,age):
        self.name=name #instance variable
        self.age=age   #instance variable

print(Person.school_name)   
p1=Person()
p1.Details("Ram",30)
p2=Person()
p2.Details("Gopal",25)

print(p1.__dict__)
print(p2.__dict__)

'''
-self.name and self.age hold data that is unique for each Person object created.
-Instance variables are unique to each object
'''

#Note:
'''
-If the values of the variable is differ then we can proceed with Instance variable like(Name and age)because they differ on every object. So,Instance b=variable is a object level variable.
-If the values of the variable is not differ then we can't use instance variable like (school_name)
'''

#In the above we have seen Instance variable creation inside the class. Now we are going to create instance variable outside the class.

#Example:
class Person:
    def __init__(self,name):
        self.name=name #instance variable inside the class
        
p1=Person("Ram")
print(p1.__dict__)
p1.age=30   #instance variable outside the class

print(p1.__dict__)

######## Accessing and deleting the Instance variable ###########