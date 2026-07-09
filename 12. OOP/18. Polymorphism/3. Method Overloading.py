# ============================================================
#                   METHOD OVERLOADING IN PYTHON
# ============================================================

"""
Definition
----------
Method Overloading means defining multiple methods with the
same name but different numbers or types of parameters.

Languages like Java and C++ support method overloading.

Python does NOT support traditional method overloading.

If multiple methods with the same name are defined in a class,
only the last method definition is retained. The previous
definitions are overwritten.
"""



# ============================================================
# ADVANTAGES OF METHOD OVERLOADING
# ============================================================

"""
Advantages
----------
1. Improves code reusability.

2. Provides flexibility to programmers.

3. Makes code easier to understand when performing
   similar operations.

4. Reduces code complexity.
"""



# ============================================================
# EXAMPLE 1 : PYTHON DOES NOT SUPPORT METHOD OVERLOADING
# ============================================================

class Test:

    def m1(self, a):
        print(a)

    def m1(self, a, b):
        print(a, b)

    def m1(self, a, b, c):
        print(a, b, c)


t = Test()

# t.m1(10)          # Error
# t.m1(10, 20)      # Error
t.m1(10, 20, 30)

"""
Output
------
10 20 30

Explanation
-----------
Although three methods with the same name (m1) are defined,
Python keeps only the last method definition.

The first two methods are overwritten.

Therefore, the class is treated as if it were written as:
"""

class Test:

    def m1(self, a, b, c):
        print(a, b, c)



# ============================================================
# EXAMPLE 2 : ACHIEVING METHOD OVERLOADING USING *args
# ============================================================

"""
Pythonic Way
------------
Since Python does not support traditional method overloading,
we can use variable-length arguments (*args) to accept any
number of arguments.
"""

class Test:

    def m1(self, *args):
        print(args)


t = Test()

t.m1(10)
t.m1(10, 20)
t.m1(10, 20, 30)

"""
Output
------
(10,)
(10, 20)
(10, 20, 30)

Explanation
-----------
The *args parameter collects all arguments into a tuple.

It allows a single method to accept any number of arguments,
which is the Pythonic alternative to method overloading.
"""



# ============================================================
# EXAMPLE 3 : USING THE multipledispatch MODULE
# ============================================================

"""
Python provides an external package called 'multipledispatch'
to achieve method overloading based on argument types.

First install the package using:

pip install multipledispatch
"""

from multipledispatch import dispatch


class Test:

    @dispatch(int, int)
    def add(self, a, b):
        print(a + b)

    @dispatch(float, float)
    def add(self, a, b):
        print(a + b)

    @dispatch(int, float)
    def add(self, a, b):
        print(a + b)

    @dispatch(int, int, int)
    def add(self, a, b, c):
        print(a + b + c)


t = Test()

t.add(10, 20)
t.add(40, 13.4)
t.add(10, 20, 30)

"""
Output
------
30
53.4
60

Explanation
-----------
The @dispatch decorator selects the appropriate method
based on the number and type of arguments passed.

Unlike normal Python methods, the multipledispatch module
supports true method overloading.
"""



# ============================================================
# SUMMARY
# ============================================================

"""
1. Python does NOT support traditional method overloading.

2. If multiple methods have the same name, only the last
   method definition is retained.

3. The recommended Pythonic approach is to use *args
   (variable-length arguments).

4. If true method overloading is required, use the
   multipledispatch module.
"""