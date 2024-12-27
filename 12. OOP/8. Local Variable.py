############# Local Variable ##########
'''
Local variable is a temporary variable to perform some operation at that particular time we can declare a temporary variable.
Local variable are created inside a function or method.
At the time of method execution local variables are created and once method execution is completed it will destroy from the memory.
We can access local variables inside the method, we can't access them outside the method.
'''
#Example:
class Calculator:
    def add(self):
        a=10  #local variable
        b=20  #local variable
        result=a+b
        print(result)
c1=Calculator()
c1.add()

#Example
class calculator:
    def add(self):
        a=10
        b=20
        result=a+b
        print(result)
        
    def sub(self):
        print(a)  #Here var a and b not works because they are local to add method
        print(b)
c1=calculator()
c1.add()
c1.sub()


