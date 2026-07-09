# ============================================================
#                    METHOD OVERRIDING
# ============================================================

"""
Definition
----------
Method Overriding means a child class provides its own
implementation of a method that already exists in the
parent class.

A parent class contains some methods, and those methods are
automatically available to the child class through inheritance.

If the child class wants different behavior, it can define
the same method with its own implementation.

This process is called Method Overriding.
"""



# ============================================================
# DOES PYTHON SUPPORT METHOD OVERRIDING?
# ============================================================

"""
Yes.

Python fully supports Method Overriding.

It is one of the important features of inheritance and is
used to achieve Runtime Polymorphism.

At runtime, Python decides which version of the overridden
method should be executed based on the object being used.
"""



# ============================================================
# RULES FOR METHOD OVERRIDING
# ============================================================

"""
Rules
-----

1. The child class must inherit from the parent class.

2. The method name in the child class must be the same
   as the method name in the parent class.

3. The method signature should generally remain the same.

4. When the method is called using a child class object,
   the child's method is executed instead of the parent's
   method.
"""



# ============================================================
# EXAMPLE 1 : CHILD USES PARENT'S METHOD (NO OVERRIDING)
# ============================================================

class Parent:

    def m1(self):
        print("This is parent m1")


class Child(Parent):
    pass


c = Child()
c.m1()

"""
Output
------
This is parent m1

Explanation
-----------
The Child class does not define its own m1() method.

Therefore, it inherits the m1() method from the Parent class.

When c.m1() is called, Python executes the inherited
parent method.
"""



# ============================================================
# EXAMPLE 2 : METHOD OVERRIDING
# ============================================================

class Parent:

    def m1(self):
        print("This is parent m1")


class Child(Parent):

    def m1(self):
        print("This is child m1")


c = Child()
c.m1()

"""
Output
------
This is child m1

Explanation
-----------
Both Parent and Child classes contain a method named m1().

The Child class overrides the Parent class method by
providing its own implementation.

Therefore, when c.m1() is called, Python executes the
Child class method instead of the Parent class method.
"""



# ============================================================
# EXAMPLE 3 : ANIMAL SOUNDS
# ============================================================

class Animal:

    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


class Cat(Animal):

    def sound(self):
        print("Cat Meows")


d = Dog()
d.sound()

"""
Output
------
Dog Barks
"""

c = Cat()
c.sound()

"""
Output
------
Cat Meows

Explanation
-----------
The Animal class defines a general sound() method.

Both Dog and Cat inherit from Animal and override the
sound() method with their own implementations.

Although the method name is the same, each child class
provides different behavior.

This demonstrates Runtime Polymorphism, where the method
that gets executed depends on the type of object created.
"""



# ============================================================
# ADVANTAGES OF METHOD OVERRIDING
# ============================================================

"""
Advantages
----------

1. Allows child classes to provide their own implementation.

2. Supports Runtime Polymorphism.

3. Improves code reusability through inheritance.

4. Makes programs flexible and easier to extend.

5. Enables different classes to respond differently to
   the same method call.
"""



# ============================================================
# SUMMARY
# ============================================================

"""
1. Method Overriding occurs when a child class defines a
   method with the same name as a method in the parent class.

2. Python fully supports Method Overriding.

3. The child class method replaces the parent class method
   for child objects.

4. Method Overriding is achieved using inheritance.

5. It is used to implement Runtime Polymorphism.

6. If the child class does not override the method,
   the inherited parent method is executed.
"""