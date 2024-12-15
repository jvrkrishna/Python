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

#OOP Calculator Example:
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")

# Create an instance of the Calculator class
calculator = Calculator()

# Perform Diffrent operations and print the result
result = calculator.add(7, 5)
print("7 + 5 =", result)

result = calculator.subtract(34, 21)
print("34 - 21 =", result)

result = calculator.multiply(54, 2)
print("54 * 2 =", result)

result = calculator.divide(144, 2)
print("144 / 2 =", result)

result = calculator.divide(45, 0)
print("45 / 0 =", result)

