from functools import reduce
d=reduce(lambda a,b:a+b,[2,3,4,5])
print(d)

from itertools import accumulate
e=list(accumulate([2,3,4,5],lambda a,b:a+b))
print(e)