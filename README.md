Enumarate Function:
            The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.The enumerate() function adds a counter as the key of the enumerate object.

Syntax:
        enumerate(iterable, start)

iterable ----------- An iterable object
start---------A Number. Defining the start number of the enumerate object. Default 0

Example:
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))

output: It returns Index(i.e., Iterable) and value
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

