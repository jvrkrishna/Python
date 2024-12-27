#What is OOP
'''
OOP is a programming paradigm to write programs efficiently.
In OOP we will develop mainly using class and object
OOP is very suitable for developing large and complex applications.
OOP follows the Code DRY approach.
In OOP we will wrap data and function into a single unit called class.
Python collects object-oriented mechanism from c++
'''

#Advantages of OOP
'''
1. Scalable
2. Reusability
3. Modularity
4. Flexibility
5. Security
'''

#Principles of OOP
'''
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
'''

#Difference between POP and OOP
#POP Calculator Example:
# Functions to perform basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Example usage of the functions
a = 10
b = 5

# Calling the functions directly
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")



#OOP Calculator Example:
# Defining a Calculator class with methods for operations
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.result = 0  # Store the result of calculations
    
    def add(self):
        self.result = self.a + self.b
        return self.result
    
    def subtract(self):
        self.result = self.a - self.b
        return self.result
    
    def multiply(self):
        self.result = self.a * self.b
        return self.result
    
    def divide(self):
        if self.b == 0:
            return "Error! Division by zero."
        self.result = self.a / self.b
        return self.result
    
    def get_result(self):
        return self.result

# Example usage of the Calculator class
calc = Calculator(10,5)

# Performing operations using the Calculator object
print(f"{calc.a} + {calc.b} = {calc.add()}")
print(f"{calc.a} - {calc.b} = {calc.subtract()}")
print(f"{calc.a} * {calc.b} = {calc.multiply()}")
print(f"{calc.a} / {calc.b} = {calc.divide()}")
print(f"Current result is: {calc.get_result()}")
