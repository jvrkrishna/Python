# ============================================================
#                 CONSTRUCTOR OVERRIDING
# ============================================================

"""
Definition
----------
Python supports Constructor Overriding.

If a child class defines its own __init__() method, it
overrides the constructor of the parent class.

When a child class has its own constructor, the parent
class constructor is NOT called automatically.

If the parent constructor also needs to be executed,
it must be called explicitly using:

    super().__init__()

or

    ParentClass.__init__(self)

This allows both constructors to execute.
"""



# ============================================================
# DOES PYTHON SUPPORT CONSTRUCTOR OVERRIDING?
# ============================================================

"""
Yes.

Python fully supports Constructor Overriding.

Whenever a child class defines its own __init__() method,
it replaces (overrides) the constructor inherited from
the parent class.

Only the child constructor is executed unless the parent
constructor is explicitly invoked.
"""



# ============================================================
# RULES FOR CONSTRUCTOR OVERRIDING
# ============================================================

"""
Rules
-----

1. The child class must inherit from the parent class.

2. The child class defines its own __init__() method.

3. The child constructor overrides the parent constructor.

4. The parent constructor is NOT called automatically.

5. To execute the parent constructor, use:

       super().__init__()

   or

       ParentClass.__init__(self)
"""



# ============================================================
# EXAMPLE 1 : CONSTRUCTOR OVERRIDING
# ============================================================

class Parent:

    def __init__(self):
        print("Parent Constructor")


class Child(Parent):

    def __init__(self):
        print("Child Constructor")


c = Child()

"""
Output
------
Child Constructor

Explanation
-----------
The Child class defines its own constructor.

Therefore, it overrides the Parent class constructor.

When a Child object is created, only the Child constructor
is executed.

The Parent constructor is not executed because it is
overridden.
"""



# ============================================================
# EXAMPLE 2 : EXECUTING BOTH CONSTRUCTORS
# ============================================================

class Parent:

    def __init__(self):
        print("Parent Constructor")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child Constructor")


c = Child()

"""
Output
------
Parent Constructor
Child Constructor

Explanation
-----------
The Child class overrides the Parent constructor.

Inside the Child constructor, super().__init__() is used
to explicitly call the Parent constructor.

Execution Order:
----------------
1. Parent constructor executes first.
2. Control returns to the Child constructor.
3. Child constructor executes.

Thus, both constructors are executed.
"""



# ============================================================
# ADVANTAGES OF CONSTRUCTOR OVERRIDING
# ============================================================

"""
Advantages
----------

1. Allows child classes to initialize their own data.

2. Provides flexibility in object initialization.

3. Enables child classes to extend the functionality of
   the parent constructor.

4. Parent constructor can still be executed using
   super().__init__().

5. Improves code reusability through inheritance.
"""



# ============================================================
# SUMMARY
# ============================================================

"""
1. Python supports Constructor Overriding.

2. If the child class defines its own __init__(),
   it overrides the parent constructor.

3. The parent constructor is NOT called automatically.

4. To execute the parent constructor, use:

       super().__init__()

   or

       ParentClass.__init__(self)

5. Using super() is the recommended and most Pythonic
   approach for calling the parent constructor.
"""