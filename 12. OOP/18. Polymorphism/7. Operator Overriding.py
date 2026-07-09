# ============================================================
#        OPERATOR OVERRIDING (OPERATOR OVERLOADING)
# ============================================================

"""
Definition
----------
Operator Overriding (also called Operator Overloading)
allows you to define how Python operators such as:

    +, -, *, /, ==, <, >, <=, >=

behave for objects of user-defined classes.

Python achieves this using special methods called
Magic Methods (or Dunder Methods).

Common Magic Methods
--------------------

+   --> __add__()

-   --> __sub__()

*   --> __mul__()

/   --> __truediv__()

==  --> __eq__()

>   --> __gt__()

<   --> __lt__()

>=  --> __ge__()

<=  --> __le__()
"""



# ============================================================
# EXAMPLE 1 : WITHOUT OPERATOR OVERRIDING
# ============================================================

class Employee:

    def __init__(self, salary):
        self.salary = salary


class Student:

    def __init__(self, stipend):
        self.stipend = stipend


e = Employee(10000)
s = Student(5000)

# print(e + s)

"""
Output
------
TypeError:
unsupported operand type(s) for +:
'Employee' and 'Student'

Explanation
-----------
Python does not know how to add an Employee object
and a Student object.

Since no __add__() method is defined, Python raises
a TypeError.
"""



# ============================================================
# EXAMPLE 2 : WITH OPERATOR OVERRIDING
# ============================================================

class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.stipend


class Student:

    def __init__(self, stipend):
        self.stipend = stipend


e = Employee(10000)
s = Student(5000)

print(e + s)

"""
Output
------
15000

Explanation
-----------
The Employee class overrides the + operator by defining
the __add__() method.

When Python evaluates:

    e + s

it automatically calls:

    e.__add__(s)

which is internally equivalent to:

    Employee.__add__(e, s)

Inside the __add__() method:

    return self.salary + other.stipend

becomes:

    10000 + 5000

Hence, the output is:

    15000
"""



# ============================================================
# WHAT HAPPENS INTERNALLY?
# ============================================================

"""
When Python encounters:

    e + s

it automatically converts it to:

    e.__add__(s)

or equivalently:

    Employee.__add__(e, s)

This automatic conversion is called Operator Overriding
(or Operator Overloading).
"""



# ============================================================
# EXAMPLE 3 : ADDING TWO NUMBER OBJECTS
# ============================================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

"""
Output
------
30

Explanation
-----------
Here,

    n1 + n2

internally becomes:

    n1.__add__(n2)

The __add__() method creates and returns a new
Number object containing:

    10 + 20 = 30

The __str__() method converts the Number object
into a string, so print() displays:

    30
"""



# ============================================================
# KEY POINTS
# ============================================================

"""
1. Operator Overriding is also called
   Operator Overloading.

2. It is achieved using Magic (Dunder)
   Methods.

3. The + operator calls __add__().

4. The - operator calls __sub__().

5. The * operator calls __mul__().

6. The / operator calls __truediv__().

7. The == operator calls __eq__().

8. The > operator calls __gt__().

9. The < operator calls __lt__().

10. Whenever Python encounters an operator on
    objects, it automatically invokes the
    corresponding magic method if it exists.
"""



# ============================================================
# INTERNAL MAPPING OF OPERATORS
# ============================================================

"""
Expression                Internal Method Call
------------------------------------------------

e + s                -->     e.__add__(s)

e - s                -->     e.__sub__(s)

e * s                -->     e.__mul__(s)

e / s                -->     e.__truediv__(s)

e == s               -->     e.__eq__(s)

e > s                -->     e.__gt__(s)

e < s                -->     e.__lt__(s)

e >= s               -->     e.__ge__(s)

e <= s               -->     e.__le__(s)
"""



# ============================================================
# SUMMARY
# ============================================================

"""
1. Operator Overriding allows operators to work with
   user-defined objects.

2. It is also known as Operator Overloading.

3. Python performs operator overriding using
   Magic (Dunder) methods.

4. If the corresponding magic method is not defined,
   Python raises a TypeError.

5. When an operator is used on objects, Python
   automatically calls the corresponding magic method.
"""