#Lambda function
'''
lambda function is a small anonymous function.
Normal function is define using de keyword and lambda function is define using lambda keyword.A Lambda function can take any number of arguments, but can only have one expression.'''
#Example:
x=lambda a,b,c:a+b
print(x(1,8,3))

print((lambda a,b:a+b)(10,20)) #we can write in one line also

#Example:
x=lambda n:n*n
print(x(5))

print((lambda n:n*n)(10))

#Example:
y=lambda a,b:a if a>b else b
print(y(10,20))

print((lambda a,b:a if a>b else b)(10,20))

#Example:
z=lambda a,b:a,b
print(z(10,20))#error beacuse lambda can take any no of arguments but have only one expression

#Example:
z=lambda a,b:(a,b) #Here it is one expression
print(z(10,20)) # it works Because it is one expression with in one entity tuple

#Where we exactly use lambda function?
'''Sometime as a programmer we have to pass function as an argument to another function, at that particular time we can go for lambda function. These functions mainly used in filter(), map(), reduce().'''
