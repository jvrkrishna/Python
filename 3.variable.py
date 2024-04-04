x=5
y="john"
print(x)
print(y)

x=4
x="ram"
print(x)

x=y=z="orange"   #Here we can one value to multi variables
print(y)

x="ram","Banti","Chanti"  #Here we can assign multi values to one variable at a time
print(x)

x,y,z="ram","Banti","Chanti"  #Here we can assign multi values to multi variables at a time
print(x)
print(z)

x="Hello"
y="World"
z=x+y
print(z)
print("Answer is:" +z)

x="Hello"
y=2
#z=x+y
print(z) #shows as an error because we cannot add number and word
print("Answer is:" +z)

a="Apple"
def myfunc():
    print(a)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)


x = "awesome"
def myfunc():
    global x  #global is a keyword which is used to change the local value as well
    x = "fantastic"
myfunc()
print("Python is " + x)

