#Reduce function:
'''The reduce() function receives two arguments, a function and an iterable. However, it doesn't return another iterable, instead it returns a single value.
Reduce function present inside the functools, so we have to import it before using reduce function.'''

#Example:
from functools import reduce
x=[10,20,30,40]
def function(a,b):
    return a+b

d=reduce(function,x)
print(d)

#Example:
from functools import reduce
d=reduce(lambda a,b:a+b,[2,3,4,5])
print(d)

#Example:
from functools import reduce
d=reduce(lambda a,b:a if a>b else b,[2,8,4,5])
print(d)

#Example:
from functools import reduce
d={1:"Rama",2:"Krishna",3:"Gopal",4:"Rambabu"}
output=reduce(lambda a,b:a+b,d.items())
print(output)

#Difference between reduce and accumulate
'''
reduce gives final output but accumulate gives iterable output
accumulate syntax:(iterable,function)
'''
#reduce example
from functools import reduce
d=reduce(lambda a,b:a+b,[2,3,4,5])
print(d)

#accumulate example
from itertools import accumulate
e=list(accumulate([2,3,4,5],lambda a,b:a+b))
print(e)