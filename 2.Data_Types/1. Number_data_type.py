#There are different data types they are:
'''
1. Number
2. String
3. List
4. Tuple
5. Set
6. Dict
'''

#Now we are discussing about Number Data Type ---- int, float, complex, Boolean
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
z = 1+10j # complex 1 real part and 10 is imaginary part
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(z.real)
print(z.imag)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


#Boolean ---- True, False
print(bool(1))
print(bool(0))

print(bool(2))
print(True)
print(False)

#input function
a=input("Enter the input:")
print(a)

#If suppose if we give specific data type it will take that type of data only as input.
a=int(input("Enter the input:"))
print(a)

print(type(a))

#But the input() default type is string.
