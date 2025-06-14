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
print(p3)