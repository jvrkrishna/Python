############# Assertion ################
'''
--->Assert is keyword in python which is used for debugging.
--->Debugging is the process of finding and fixing bugs.
--->If we want to verify something then we can use assertion.
'''

#Example:
a=100
print(1)
print(2)
assert a==100 #If the cond is true then execute next code, If it is false raise exception and stop the flow of execution.
print(3)
print(4)

#Example:
a=100
print(1)
a=20
print(2)
assert a==100 #AssertionError because a is updated to 20
print(3)
print(4)

#Example: By default Assertion Not gives any message in this example we will give Message
a=100
print(1)
a=20
print(2)
assert a==100," a value is updated" #message
print(3)
print(4)

#Example:
x = 5
assert x > 0, "x should be positive"
assert x < 3, "Sorry X is not less than 3"

#Example:
l=["Ram","Gopi","Seetha"]
assert input("Enter your name:") in l, "This name is not present"
print(l)

#Example:
l=["Ram","Gopi","Seetha"]
try:
    assert input("Enter your name:") in l, "This name is not present"
except AssertionError as e:
    print(e)
print(l)

#Example: without Assert
def prime_number(n):
    if n>1:
        counter=0
        for i in range(1,n+1):
            if n%i==0:
                counter+=1
        if counter==2:
            return "Given number is a prime number"
        else:
            return "Given number is not a prime number"
    else:
        return "Prime number only above one not less than or negative numbers"
print(prime_number(5))
print(prime_number(4))
print(prime_number(0))

#Example: With Assertion
def prime_number(n):
    assert n>1,"Prime number only above one not less than or negative numbers"
    counter=0
    for i in range(1,n+1):
        if n%i==0:
            counter+=1
    if counter==2:
        return "Given number is a prime number"
    else:
        return "Given number is not a prime number"
print(prime_number(5))
print(prime_number(4))
print(prime_number(0))

'''
1. Simple Assertion:
A basic check to make sure a value is true.
'''
age = 25
assert age >= 18, "Age must be 18 or older"
'''If age is less than 18, an AssertionError will be raised with the message "Age must be 18 or older".'''

'''
2. Checking List Length:
You can use assertions to validate that a list has the correct number of elements.
'''

names = ["Alice", "Bob", "Charlie"]
assert len(names) == 3, "List must contain exactly 3 names"
'''If the list length is not 3, an error will be raised.'''

'''
3. Type Checking:
Assertions can be used to ensure a variable is of the expected type.
'''

value = 10.5
assert isinstance(value, float), "Value should be a float"
'''If value is not a float, it will raise an error.'''

'''
4. Check for Non-empty String:
You can assert that a string is not empty.
'''
username = "john_doe"
assert username, "Username cannot be empty"
'''If username is an empty string, the assertion will fail.'''

'''5. Dividing by Zero Prevention:
Before performing division, we can assert that the denominator is not zero.
'''

denominator = 5
assert denominator != 0, "Denominator cannot be zero"
result = 10 / denominator
print(result)
'''If denominator is 0, an assertion error will occur before the division happens.'''

'''6. Complex Condition:
You can use more complex conditions within assertions, such as checking if a number is within a valid range.'''
score = 85
assert 0 <= score <= 100, "Score must be between 0 and 100"
'''If score is outside the valid range (0 to 100), the assertion will fail.'''

'''
7. Using Assertions in Functions:
Assertions are also useful within functions to ensure input validity.
'''
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

result = divide(10, 2)  # Works fine
# result = divide(10, 0)  # Will raise AssertionError
'''
8. Using Assertions in Loops:
Assertions can be helpful inside loops to ensure consistency or check conditions for each iteration.
'''
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    assert num > 0, f"Invalid number: {num}, it must be positive"
'''If any number in the list is less than or equal to 0, the assertion will raise an error.'''

'''9. Testing Complex Data Structures:
You can use assertions to test conditions in complex data structures, such as dictionaries.'''
user_data = {"name": "Alice", "age": 30}
assert "name" in user_data, "Name is missing"
assert user_data["age"] >= 18, "Age must be 18 or older"
'''
10. Using Assertions with Custom Objects:
You can also assert conditions on custom objects (e.g., objects of a class).
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        assert self.price >= 0, "Price cannot be negative"
        self.price *= 0.9  # Apply a 10% discount

product = Product("Laptop", 1000)
product.apply_discount()  # Works fine
# product.price = -100  # Will raise AssertionError
