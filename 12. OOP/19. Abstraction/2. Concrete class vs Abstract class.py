#### Concreate class vs Abstract class #####

#Concrete Class:
'''
--->Class contain concreate method, we can not use abstract method.
--->Child class is not responsible to provide any implementation part for parent class.
--->We can create the object of class. 
--->Class is the buleprint for object.
--->To define concreate class we don't required to import any module.
'''

#Abstract Class:
'''
--->Abstract class can contain abstract methods as well as concreate method.
--->Child class is responsible to provide implementation part for parent class.
--->We can not create object for abstract class.
--->Abstract class is the blueprint for class.
--->To define abstract class we required to imprt abc module and extends from ABC class.
'''

#Example: General Example of class Creation.
class Test:
    def m1(self):
        pass
t=Test()
t.m1()  #It executes normally

#Example:Abstract class with abstract method
from abc import ABC, abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass
t=Test() 
#TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'm1'. i.e., we cannot create object for abstact class.

#Example: Abstract class without abstract method
from abc import ABC, abstractmethod
class Test(ABC):
    def m1(self):
        pass
t=Test()  #It executes normally no issues

#Abstract class with abstract method with implementation. 
from abc import ABC, abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class Child(Test):
    def m1(self):
        print("Hello")
c=Child()
c.m1()

#Abstract class with abstract method with implementation. 
from abc import ABC, abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class Child(Test):
    def m1(self):
        pass #Here body has nothing it executes because we have implemented the method with nothing
c=Child()
c.m1()

#Abstract class with abstract method with implementation. 
from abc import ABC, abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self):
        pass

class Child(Test):
    pass #Here m1 method is not implemented then it gives error
c=Child()
c.m1()
