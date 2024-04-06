a=10.7 #here we cannot delare data type because python is dynamically typed
print(a)
print(type(a))
print(id(a))

a="Rama krishna"
print(a)
print(type(a))
print(id(a))

x = 8 # int
y = 2.8  # float
z = 1j   # complex
# To verify the type of any object in Python, use the type() function:
# Example
print(type(x))
print(type(y))
print(type(z))


x = 1 # int
y = 2.8 # float
z = 1j # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


import random
print(random.randrange(1,5))

