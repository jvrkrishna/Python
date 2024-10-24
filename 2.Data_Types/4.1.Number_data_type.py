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


# SOME IMP INBUILT FUNCTIONS Before concept :

# Random Number
'''Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:'''

# Example
import random
print(random.randrange(1,10))

#input function
a=input("Enter the input:")
print(a)

#If suppose if we give specific data type it will take that type of data only as input.
a=int(input("Enter the input:"))
print(a)

print(type(a))

#But the input() default type is string.

# Types to print the output

# 1.Print with the print function
X=10
print(X)

# 2.Print with string formatting %
name="Rama Krishna"
age=29
print("My name is %s and my age is %d"%(name,age))

# 3.Print with the str.format() method
age=29
print("My name is {} and my age is {}".format(name,age))

name1="Gopal"
print("My name is {name} and my age is {age}".format(name=name1,age=age))

course="Python"
price=2.99 #print this is dollar format
print("My course is {} and the price is ${price:.1f}".format(course,price=price))

# 4.Print with the ‘f-string’ 
name="Rama Krishna"
print(f"my name is {name}")

salary=10000
tax=0.2
print(f"my monthly salary is ${salary-tax}")

# 5.Print to a file or a stream
#printing to a file
with open('result.txt','w') as f:
    print("This will retun to a file", file=f)

#printing to a stream  
import sys
print("This will return to a stream", file=sys.stderr)


