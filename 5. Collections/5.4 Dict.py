#By using List, Tuple, Set we can store only values
#Sometimes as a programmer we require to key and value as a pair in that case we can go to dictionary.

# empty dictionary 
my_dict = {}    #my_dict=dict()
print(my_dict)

# empty dictionary 
my_dict = {}
my_dict['name']="Rama"
print(my_dict)

# dictionary with integer keys 
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)
print(my_dict[1])

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)
print(my_dict['name'])

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)

# from sequence having each item as a pair 
my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)
