# ============================================================
#                    OPERATOR OVERLOADING
# ============================================================

"""
Definition
----------
Operator Overloading means using the same operator for different purposes depending on the operands (objects) on which it is used.

For example, the + operator is used for:
1. Addition of numbers.
2. Concatenation of strings.

Python supports operator overloading using Magic (Dunder) methods.

Languages like Java do not allow user-defined operator overloading
(except the built-in behavior of + for strings).
"""

# ------------------------------------------------------------
# Example
# ------------------------------------------------------------

print(10 + 20)            # Addition
print("Ram" + "Krishna")  # String Concatenation

"""
Output
------
30
RamKrishna

Explanation
-----------
The + operator performs different operations depending on
the operands.

• Addition for numbers.
• Concatenation for strings.
"""



# ============================================================
# WITHOUT OPERATOR OVERLOADING
# ============================================================

"""
Without Operator Overloading
----------------------------
If we do not overload operators, we cannot use operators such as
+ or == directly on user-defined objects.

Instead, we create normal methods like add() or isEqual() and
call them explicitly.
"""



# ------------------------------------------------------------
# 1. Addition Without Operator Overloading
# ------------------------------------------------------------

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Example

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1.add(p2)
print(p3)

"""
Output
------
Point(4, 6)

Explanation
-----------
Here we use the add() method instead of the + operator.

No operator overloading is involved.
"""



# ------------------------------------------------------------
# 2. Equality Without Operator Overloading
# ------------------------------------------------------------

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isEqual(self, other):
        return self.x == other.x and self.y == other.y


# Example

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1.isEqual(p2))
print(p1.isEqual(p3))

"""
Output
------
True
False

Explanation
-----------
Instead of using ==, we explicitly call the isEqual() method.

This does not use operator overloading.
"""



# ============================================================
# WITH OPERATOR OVERLOADING
# ============================================================

"""
Operator Overloading
--------------------
Python allows operators to work with user-defined objects by
implementing special methods called Magic (Dunder) methods.

For example:

+  --> __add__()
== --> __eq__()

Whenever an operator is used, Python automatically calls the
corresponding magic method.
"""



# ------------------------------------------------------------
# 1. Overloading the + Operator
# ------------------------------------------------------------

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Example

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3)

"""
Output
------
Point(4, 6)

Explanation
-----------
The + operator automatically calls the __add__() method.

The __add__() method returns a new Point object containing
the sum of the corresponding x and y values.

Note
----
If __add__() returns:

    return self.x + other.x, self.y + other.y

Then the output will be:

    (4, 6)

because Python returns a tuple.

To get:

    Point(4, 6)

return a Point object and define the __str__() method.
"""



# ------------------------------------------------------------
# 2. Overloading the == Operator
# ------------------------------------------------------------

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Example

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)
print(p1 == p3)

"""
Output
------
True
False

Explanation
-----------
Whenever the == operator is used between two Point objects,
Python automatically calls the __eq__() method.

The __eq__() method compares the x and y values of both
objects and returns True if both are equal; otherwise,
it returns False.
"""



# ============================================================
# DIFFERENCE BETWEEN WITH AND WITHOUT OPERATOR OVERLOADING
# ============================================================

"""
Without Operator Overloading
----------------------------
• Uses normal methods such as add() and isEqual().

• Methods must be called explicitly.

• Examples:
      p1.add(p2)
      p1.isEqual(p2)

• Less readable.

• More code is required.


With Operator Overloading
-------------------------
• Uses operators such as + and ==.

• Operators automatically call magic methods.

• Examples:
      p1 + p2
      p1 == p2

• More readable and natural.

• Less code is required.
"""



# ============================================================
# COMMON MAGIC METHODS FOR OPERATOR OVERLOADING
# ============================================================

"""
Operator          Magic Method
--------------------------------------------

+              -->    __add__(self, other)

-              -->    __sub__(self, other)

*              -->    __mul__(self, other)

/              -->    __truediv__(self, other)

//             -->    __floordiv__(self, other)

%              -->    __mod__(self, other)

**             -->    __pow__(self, other)

==             -->    __eq__(self, other)

!=             -->    __ne__(self, other)

<              -->    __lt__(self, other)

<=             -->    __le__(self, other)

>              -->    __gt__(self, other)

>=             -->    __ge__(self, other)
"""