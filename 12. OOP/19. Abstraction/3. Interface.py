########## Interface ###############
'''
--->If the class holds only abstract methods then it is known as Interface. Where abstract class contain abstract as well as concreate method.
--->Python doesn't provide any support for interface, so we must define by using abc module.
--->we can't create object for interface.
--->Interface is the blueprint for class.
--->Child is responsible to provide the body part for interface abstract methods.
'''
#A normal class will hold all the concrete methods.
#An abstract class will hold both concrete and abstract methods.
#An interface will only hold abstract methods.

#Example:
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