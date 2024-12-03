#Generator function:
'''A generator-function is defined like a normal function, but whenever it needs to generate a value, it does go with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.'''
'''The difference between the yield and the return statement in Python is:
Return: A function that returns a value at once. The return statement returns a value and exits the function altogether.
Yield: A function that yields values repeatedly. The yield statement pauses the execution of a function and returns a value.
When called again, the function continues execution from the previous yield. A function that yields values is known as a generator.'''

#Example:
# A Python program to demonstrate use of generator object with next() 

# A generator function 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simpleGeneratorFun() 

# Iterating over the generator object using next 

# In Python 3, __next__() 
print(x.__next__())
print(next(x)) 
print(next(x))

#Example:
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

# Driver code to check above generator function 
for i in simpleGeneratorFun(): 
	print(i)
 
#Example:
def simpleGeneratorFun(): 
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n=n+1

# Driver code to check above generator function 
for i in simpleGeneratorFun(): 
	print(i)