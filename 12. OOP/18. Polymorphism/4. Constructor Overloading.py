# ============================================================
#                CONSTRUCTOR OVERLOADING IN PYTHON
# ============================================================

"""
Definition
----------
Constructor Overloading means creating multiple constructors
with different parameter lists (different number or types of
arguments).

Languages such as Java and C++ support constructor overloading.

Python does NOT support constructor overloading directly.

If multiple __init__() methods are defined in the same class,
only the last definition is retained, and all previous
definitions are overwritten.
"""



# ============================================================
# EXAMPLE 1 : CONSTRUCTOR OVERLOADING IS NOT POSSIBLE
# ============================================================

class Test:

    def __init__(self, a):
        print(a)

    def __init__(self, a, b):
        print(a, b)


# t = Test(10)      # Raises an error

"""
Output
------
TypeError:
Test.__init__() missing 1 required positional argument: 'b'

Reason
------
The first __init__() method is overwritten by the second one.

Therefore, Python treats the class as if it contains only:

    def __init__(self, a, b):
        ...

Hence, creating an object with only one argument results
in a TypeError.
"""



# ============================================================
# METHOD 1 : USING VARIABLE-LENGTH ARGUMENTS (*args)
# ============================================================

"""
Pythonic Approach
----------------
The most common way to simulate constructor overloading in
Python is by using variable-length arguments (*args).

The *args parameter allows the constructor to accept any
number of arguments.
"""

class Test:

    def __init__(self, *args):
        print(args)


t = Test(10)
t1 = Test(10, 20)

"""
Output
------
(10,)
(10, 20)
"""



# ------------------------------------------------------------
# Processing Arguments Based on Their Count
# ------------------------------------------------------------

class Test:

    def __init__(self, *args):

        if len(args) == 1:
            print("One argument:", args[0])

        elif len(args) == 2:
            print("Two arguments:", args[0], args[1])

        else:
            print("Invalid arguments")


t = Test(10)
t1 = Test(10, 20)

"""
Output
------
One argument: 10
Two arguments: 10 20

Explanation
-----------
The constructor checks the number of arguments using len(args)
and performs different actions accordingly.

This is the most commonly used technique for simulating
constructor overloading in Python.
"""



# ============================================================
# METHOD 2 : USING THE multipledispatch MODULE
# ============================================================

"""
The multipledispatch package allows method dispatching based
on the number and types of arguments.

First install the package using:

pip install multipledispatch
"""

from multipledispatch import dispatch


class Test:

    @dispatch(int)
    def __init__(self, a):
        print("One integer:", a)

    @dispatch(int, int)
    def __init__(self, a, b):
        print("Two integers:", a, b)


t = Test(10)
t1 = Test(10, 20)

"""
Output
------
One integer: 10
Two integers: 10 20

Explanation
-----------
The @dispatch decorator selects the appropriate constructor
based on the type and number of arguments.

Although this provides constructor overloading, it is not
commonly used in real-world Python applications.
"""



# ============================================================
# METHOD 3 : USING DEFAULT ARGUMENTS (RECOMMENDED)
# ============================================================

"""
Another Pythonic way to simulate constructor overloading is
by using default arguments.

This is the recommended approach because it is simple,
readable, and does not require external libraries.
"""

class Test:

    def __init__(self, a, b=None):

        if b is None:
            print("One argument:", a)

        else:
            print("Two arguments:", a, b)


t = Test(10)
t1 = Test(10, 20)

"""
Output
------
One argument: 10
Two arguments: 10 20

Explanation
-----------
The parameter b has a default value of None.

If only one argument is supplied, b remains None.

If two arguments are supplied, both values are processed.

This is the preferred way of handling constructor overloading
in Python.
"""



# ============================================================
# NOTE
# ============================================================

"""
Using multipledispatch with __init__() is uncommon in
real-world Python projects.

Most Python developers prefer using one of the following:

1. Variable-length arguments (*args)

2. Default arguments

3. Class methods (alternative constructors)
"""



# ============================================================
# SUMMARY
# ============================================================

"""
1. Python does NOT support traditional constructor overloading.

2. If multiple __init__() methods are defined, only the last
   one is retained.

3. Constructor overloading can be simulated using:

   • Variable-length arguments (*args)
   • Default arguments (Recommended)
   • multipledispatch module
   • Class methods (alternative constructors)

4. The most Pythonic and commonly used approaches are:

   • *args
   • Default arguments
"""