#Instance variables ----- Instance variables means where we are initialising variable with self
'''
create
modify
access
del --- all these operation we can do in constructor, instance method, and outside the class
'''

#Creation of instance variable
class sample:
    def __init__(self,name):
        self.name=name   #Instance variable inside constructor
        
    def m1(self,age):
        self.age=age   #Instance variable inside instance method
        
        
s=sample("Rama")
s.m1(30)
s.address="Kakinada" #Instance variable outside class
print(f"My name is {s.name} and my age is {s.age} and my address is {s.address}")
        
#Note:
'''
-If the values of the variable is differ then we can proceed with Instance variable like(Name and age)because they differ on every object. So,Instance variable is a object level variable.
-If the values of the variable is not differ then we can't use instance variable we can use only static variables like(school_name)
'''
#Modify of instance variable
class sample:
    def __init__(self,name,age):
        self.name=name   #Instance variable 
        self.age=age     #instance variable 
        if self.age<18:  #instance variable modification inside the constructor
            self.status="Minor"
        else:
            self.status="Adult"
        
    def m1(self,nname,address):
        self.name=nname   #Instance variable modification inside the instance method
        self.address=address #instance variable
        
        
s=sample("Rama",int(input("Enter the age:")))
s.m1("raju","Kakinada")
s.address="Rajahmundry"
print(f"My name is {s.name} and my age is {s.age} and status is {s.status} and address is {s.address}")


#Accessing the instance variables
class sample:
    def __init__(self,name):
        self.name=name
        print(f"My name is {self.name}") #Accessing inside the constructor
        
    def m1(self):
        print(f"My name is {self.name}") #Accessing inside the instance method
        
s=sample("Rama")
s.m1()
print(f"My name is {s.name}")  #accessing inside outside the class
        
#Deleting the instance variables
class sample:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        del self.name  #deleting variable inside the constructor
                
    def m1(self):
        del self.age   #deleting  variable inside the instance method
        
s=sample("Rama",30,"kakinada")
del s.address   #deleting variable outside the class
print(f"My name is {s.name}  and my age is {s.age} and my address is {s.address}") 
        