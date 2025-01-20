#What is Class
'''
class is a blue print of object. It is logical entity and it is virtual not real.
If we want to create an object, then we required a blueprint and that blueprint is known as class. Collection of object is known as class.
Inside class we will represent properties(variables) and behaviours(methods).
'''

#Example
'''
Suppose we have the class like Student.
For Student have some properties like SName, Sage, SAddress, SID.
For Student have some methods like Eating, Sleeping, Reading, Playing.
'''

#Syntax for class:
'''
class classname:
    #properties
    #methods
'''
    
#what is Object
'''
object is real entity and it is a physical entity.
Object is the instance of class.
Objects are created inside the Heap Memory.
we can create any number of objects by using class.
'''

#Syntax for Object:
'''
reference_variable=classname(arguments)
'''

#What is reference variable
'''
Reference varaible is used to refer to an object
Reference variable is acting as an accessor.
Reference variable is used to access properties and methods of an object.
Multiple objects can point to the same object.
'''

#Example:
a=10   #Here a is reference variable which is stored in stack memory and value 10 is an object which is stored in Heap memory.

#Example 1
class Student:
    '''Here marks is a property(i.e.,variable) and sample() is behaviour(i.e., method) '''
    marks=10
    def sample(self):  
        print("Hello World")
#In above lines we have created plan nothing but class and we go implement on below lines.
# when we are creating method then definitely pass atleast one argument "self" keyword  

#Creating object by using class with the help of reference variable s1 and calling the propertys and methods.
s1=Student()
print(s1.marks)
s1.sample()

#Example 2
class Student:
    marks=10
    def sample(self,name,age):
        print(f"My name is {name}, my age is {age} and marks are {Student.marks}")
        
s1=Student()
print(s1.marks)
s1.sample("Gopal",30)

#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created
#Here no need to call with object (app.__init__(10)). It will execute directly when object created.
#Here init is a constructor as well as method used to assign values to instance variable

#Example 3
class Student:
    def __init__(self,name,age):   #Here __init__ is constructor
        self.n=name
        self.a=age
    def details(self):
        print(f"My name is {self.n} and my age is {self.a}")
        
s1=Student("gopal",30)  #At the time of object creation __init__ constructor will execute auto
s1.details()

#For Explanation refer the image "Class_object Image" in Images folder

#Example 4: print the details with different methods
class Student:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def My_name(self):
        print(f"My name is {self.n}")
        
    def My_age(self):
        print(f"My age is {self.a}")
        
s1=Student("gopal",30)
s1.My_name()
s1.My_age()