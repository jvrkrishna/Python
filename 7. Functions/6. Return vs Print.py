##### return vs print
'''In functions internally return a value by default as None'''
#Example:
def add(a):
    print(a)

print(add(10))  #Here it will return None because we not returning any thing.  10  None

#Example
def add(a):
    print(a)
    return a-5

print(add(10))  #10  5

#Example
def add():
    list=[10,20,30]
    return list

print(add()) 

#Example:
def sample():
    print("Hello")

print(sample())   #Hello   None

#Example:
def sample():
    print("Hello")
    return 10

print(sample())   #Hello   10   #return replace None value

'''return statement only be at end of the function. If we give return statement in the middle after return statement remaining statement will not going to be executed.'''
#Python function can return multiple values.
def sample(a,b,c):
    return a,b,c

print(sample(10,20,30))