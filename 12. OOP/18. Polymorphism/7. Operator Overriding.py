#### Operator Overriding #####
'''operator overriding (also called operator overloading) is possible in Python. This allows you to define how operators such as +, -, *, ==, and others behave when applied to instances of a custom class.

In Python, you can override operators by defining special methods in your class. These methods are often called "dunder" methods (short for "double underscore"), such as __add__, __sub__, __mul__, __eq__, and so on.

Examples of operator overriding:
1. Overloading the + operator:
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This calls the __add__ method
print(p3)  # Output: Point(4, 6)
'''In this example, the + operator for Point objects is overridden by the __add__ method.'''

'''2. Overloading the == operator:'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False

'''
Common operator methods to override:
__add__(self, other) for +
__sub__(self, other) for -
__mul__(self, other) for *
__truediv__(self, other) for /
__eq__(self, other) for ==
__lt__(self, other) for <
__le__(self, other) for <=
__gt__(self, other) for >
__ge__(self, other) for >=
__ne__(self, other) for !=
'''