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

