##### Abstract Class and Abstract Method #####
'''
--->Partial Implementation of a class is called as abstract class.
--->Partial implementation means not complete implementation.
--->Abstract class is the blueprint for other classes.
--->Abstract class contain at least one abstract method.
--->Python doesn't provide support for abstract class, so we have to import a module named as abc module.
--->abc module stands for abstract base class.
--->Abstract class can also contain concreate method.
--->Abstract method means a method without having body part is called abstract method.
--->If we don't know the body part of a method then at that particular time we can define abstract method.
--->By using @abstractmethod decorator we can abstract method.
--->Child class will provide the body part of abstract method.
--->We can create the object of a abstract class. 
--->If a method have body part then that method is called as concreate method.
'''

#Example of Using abc Module and ABC Class:
from abc import ABC, abstractmethod #Here abc module ABC class

# Define an abstract base class
# Animal class is child class of ABC
class Animal(ABC):
    # Abstract method (must be implemented by subclasses)
    #Method not having any implementation(no body part)
    @abstractmethod
    def sound(self):
        pass
    # Concrete method (can be inherited as-is)
    def sleep(self):
        print("This animal is sleeping.")

# Define a Child class that inherits from Animal
class Dog(Animal):
    # Implement the abstract method
    def sound(self):
        print("Woof! Woof!")

# Create instances
# animal = Animal()  # This will raise an error because Animal is abstract
dog = Dog()
dog.sound()  # Outputs: Woof! Woof!
dog.sleep()  # Outputs: This animal is sleeping.

   
'''Example of Using abc Module and ABC Class:'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print("This animal is sleeping.")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")
        
# animal = Animal()  # This will raise an error because Animal is abstract
dog = Dog()
dog.sound()
dog.sleep() 

#Use of Abstract Class:
'''An abstract class is used to define a blueprint for other classes. It provides a common structure with methods that must be implemented in the child classes. If we dont know the complete implementation while creating class then we go for abstract class'''
#Example:
from abc import ABC, abstractmethod

# Abstract class Vehicle
class Vehicle(ABC):

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def Color(self):
        pass

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def Model(self):
        pass

# Concrete subclass for Vehicle
class car(Vehicle):
    def __init__(self, company):
        self.company = company

    def Color(self,colr):
        print(f"My car Company is {self.company} and the color is {colr}")

    def Model(self,mdl):
        print(f"My {self.company} car belongs to {mdl}")
        
#We can create n no of concrete subclasses for Vehicle like above

# Instantiate objects
c = car("Suzuki")
c.Color("Red")
c.Model(2020)


