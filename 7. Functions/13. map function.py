#Map function:
'''map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax :
map(fun, iter)
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Note: In this some modification on every element.'''

#Example:
ages=[10,20,30,40,50]
def function(n):
    return n+n

result=map(function,ages)
print(list(result))


#Example by using map with lambda
print(list(map(lambda x:x+x,ages)))


#Wap to print merging of two lists
a=[10,20,30,40,50]
b=[1,2,3,4,5,6]
print(list(map(lambda i,j:i+j,a,b)))
