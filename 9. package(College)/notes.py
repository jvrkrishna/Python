#What is Package
'''
Package is nothing but folder or directory.
package is a container where we can store similar sub-packages and modules.
'''

# __init__.py
'''
If a folder contains __init__.py file then it will be considered a python package(It is optional after python 3.2 version).
This __init__.py can be empty.
'''

#Example structure follow college
'''
college
    staff
        __init__.py
        teaching.py   
        non_teaching.py
    students
        __init__.py
        arts.py
        sceince.py
    __init__.py
    info.py
'''

"""
College_program.py
"""

#Think of it like this:
'''Module = one Python file (.py)
Package = a folder containing multiple modules

Example: Creating a Package
Suppose we want to create a package called calculator.

Folder Structure
calculator/
│
├── __init__.py
├── addition.py
├── subtraction.py
└── multiplication.py'''

#addition.py
def add(a, b):
    return a + b

#subtraction.py
def subtract(a, b):
    return a - b

#multiplication.py
def multiply(a, b):
    return a * b

#init.py
from .addition import add
from .subtraction import subtract
from .multiplication import multiply

#Using the Package
#Create another file named main.py.
import calculator
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))

Output:
15
5
50

#Importing Individual Modules
#You can also import specific modules:
from calculator.addition import add
print(add(20, 30))

Output:
50

#Real-Life Example
#Python's standard library contains many packages:
import math
print(math.sqrt(25))

Output:
5.0

#Here, math is a module. A package example is:
import email

#The email package contains several modules like:

email.message
email.utils
email.mime

'''Why Use Packages?
Organizes code into logical groups.
Avoids name conflicts between modules.
Makes projects easier to maintain.
Promotes code reuse.

#Best Real-World Example

Imagine an e-commerce application:

ecommerce/
│
├── products/
│   ├── add_product.py
│   └── search_product.py
│
├── orders/
│   ├── create_order.py
│   └── cancel_order.py
│
└── payments/
    ├── credit_card.py
    └── upi.py

Usage:
from ecommerce.payments.upi import pay
pay(1000)

This structure keeps large applications clean and easy to manage.'''
