##########Instance variable####################
'''
Instance variables are variables that belong to a specific instance (object) of a class.
'''

#########Creation of Instance varaibles#############
#Example 1: Create a variable inside the constructor
class Person:
    def __init__(self,name,age):   #constructor
        self.name=name #instance variable
        self.age=age   #instance variable
        
p1=Person("Ram",30)   #p1 is one instance
p2=Person("gopal",25) #p2 is one instance

print(p1.__dict__)
print(p2.__dict__)

#Example 2:Create a variable inside the instance method
class Person:
    def Details(self,name,age):   #instance method
        self.name=name #instance variable
        self.age=age   #instance variable
        
p1=Person()
p1.Details("Ram",30)
p2=Person()
p2.Details("Gopal",25)

print(p1.__dict__)
print(p2.__dict__)

#Example 3:Creation of Instance variable outside the class
class Person:
    def __init__(self,name):
        self.name=name #instance variable inside the class
        
p1=Person("Ram")
print(p1.__dict__)
p1.age=30   #instance variable outside the class

print(p1.__dict__)

'''
-self.name and self.age hold data that is unique for each Person object created.
-Instance variables are unique to each object
'''

#Note:
'''
-If the values of the variable is differ then we can proceed with Instance variable like(Name and age)because they differ on every object. So,Instance variable is a object level variable.
-If the values of the variable is not differ then we can't use instance variable we can use only static variables like(school_name)
'''
###########Modify Instance variable ############
#Example 1:Modify the instance variable inside the constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        if self.age<18:
            self.status="Minor"
        else:
            self.status="Adult"

        
p1=Person("Ram",30)
print(p1.__dict__)

#Example 2:Modify the instance variable inside the Instance method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def modify(self,new_age):
        self.age=new_age

        
p1=Person("Ram",30)
print(p1.__dict__)

p1.modify(35)
print(p1.age)

#Example 3:Modify the instance variable outside the class 
class Person:
    def __init__(self,name):
        self.name=name
        
p1=Person("Ram")
print(p1.__dict__)
p1.name="gopal" 

print(p1.__dict__)

######## Accessing Instance variable ###########
#Example 1:Accessing the instance variable inside the Constructor
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age   
        print(f"My name is {self.name} and my age is {self.age}")
p1=Person("Ram",30)

#Example 2:Accessing the instance variable inside the Instance Method
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age   
    
    def detials(self):
        print(f"My name is {self.name} and my age is {self.age}")
p1=Person("Ram",30)
p1.detials()

#Example 3:Accessing the instance variable outside the class 
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age   
p1=Person("Ram",30)
print(f"My name is {p1.name} and my age is {p1.age}")

######## Delete Instance variable ###########
#Example 1: Delete the instance variable inside the Constructor
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age  
        del self.age
p1=Person("Ram",30)
print(p1.__dict__)

#Example 2: Delete the instance variable inside the Instance method
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age  
    def deleteDetails(self):
        del self.age 
p1=Person("Ram",30)
print(p1.__dict__)

p1.deleteDetails()
print(p1.__dict__)

#Example 3: Deletion the instance variable outside the class
class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age  
p1=Person("Ram",30)
print(p1.__dict__)

del p1.age
print(p1.__dict__)
