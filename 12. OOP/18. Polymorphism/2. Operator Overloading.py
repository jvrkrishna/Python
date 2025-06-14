######## Operator Overloading #######
'''
-->If we will use same operator in different purposes then it is called operator overloading.
-->we are using +, * and etc in operator for different purposes.
-->Python supports operator overloading other languages like java does not support it.
-->we will use corresponding magic method to overload operator.
'''
#Ex:
print(10+20)
print('Ram'+'Krishna')
'''In the above example operator work in different formats like adding, concatination'''

'''
1. Overloading the + operator:
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return self.x + other.x, self.y + other.y

# Example usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This calls the __add__ method
print(p3)  # Output: Point(4, 6)


'''2. Overloading the == operator:'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Example usage
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False

'''
Common operator methods to overload:
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