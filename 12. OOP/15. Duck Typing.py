# ==========================
# Duck Typing in Python
# ==========================

"""
#Definition:
Duck Typing is a concept in Python where the type of an object is not important. Python only checks whether the object has the required methods or attributes.

## Famous Rule:
"If it looks like a duck, swims like a duck, and quacks like a duck,
then treat it as a duck."

## In simple words:
Python does NOT ask:
"What class are you?"

Python asks:
"Can you do this job?"
"""
# ==========================================================
# Example 1: Same Method in Different Classes
# ==========================================================

class A:
    def m1(self):
        print("A-m1")

class B:
    def m1(self):
        print("B-m1")

class C:
    def m1(self):
        print("C-m1")

def search(x):
    x.m1()
"""
This function expects an object that has m1().
It does not care whether x is A, B, or C.
""" 
search(A())
search(B())
search(C())
"""
Output:
A-m1
B-m1
C-m1

## Explanation:
All three classes have m1(), so all objects work.
This is Duck Typing.
"""

# ==========================================================
# Example 2: Duck and Whale
# ==========================================================
class Duck:
    def swim(self):
        print("Duck is swimming")

    def fly(self):
        print("Duck is flying")

class Whale:
    def swim(self):
        print("Whale is swimming")

def action(x):
    x.swim()
    x.fly()
"""
This function expects:
1. swim()
2. fly()
"""
action(Duck())       # Works
# action(Whale())    # Error
"""
Output:
Duck is swimming
Duck is flying

If we execute:
action(Whale())

## Output:
Whale is swimming
AttributeError:
'Whale' object has no attribute 'fly'

## Explanation:
Whale has swim() but does not have fly().
Therefore Duck Typing fails at runtime.
"""

# ==========================================================
# Example 3: Real-Time Payment System
# ==========================================================
class CreditCard:
    def pay(self, amount, tax):
        print(f"Paid ₹{amount + tax} using Credit Card")

class UPI:
    def pay(self, amount, tax):
        print(f"Paid ₹{amount - tax} using UPI (discount applied)")

class Wallet:
    def pay(self, amount, tax):
        print(f"Paid ₹{amount * tax} using Wallet (reward points applied)")

def checkout(payment_method):
    payment_method.pay(1000, 100)
"""
checkout() only expects a pay() method.
It does not care about the object's class.
"""

checkout(CreditCard())
checkout(UPI())
checkout(Wallet())

"""
Output:
Paid ₹1100 using Credit Card
Paid ₹900 using UPI (discount applied)
Paid ₹100000 using Wallet (reward points applied)

## Explanation:
All payment classes have pay() method.
Therefore checkout() can work with all of them.
This is a real-world example of Duck Typing.
"""

# ==========================================================
# Advantages of Duck Typing
# ==========================================================

"""
1. Flexible
   Different objects can be used in the same function.

2. Less Code
   No need for many if-else or isinstance() checks.

3. Easy to Extend
   New classes can be added without changing old code.

4. Supports Polymorphism
   Same function works with different objects.
   """
# ==========================================================
# Disadvantage of Duck Typing
# ==========================================================
"""
If the required method is missing,
Python raises an error at runtime.

## Example:
AttributeError:
'Whale' object has no attribute 'fly'
"""
