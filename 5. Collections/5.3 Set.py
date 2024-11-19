#Creation of Empty set is bit tricky

# s={}
# print(s)
# print(type(s))  #basically it is dictionary

#Here it will crate empty dict. Instead of empty set.
#{} symbol is also used to create dict.
#We can create empty set by using set()

s=set()
print(s)
print(type(s))

#Creation of set with multiple elements:
s={10,20,30,40,50}
print(s)
print(type(s))

#Creation of set with heterogenous elements.
s={30,"Ram",65.4,True}
print(s)
print(type(s))

#Creation of set from list
l1=[10,20,30,40,50]
s1=set(l1)
print(l1)
print(type(l1))

#Creationm of set from range()
s=set(range(10))
print(s)
print(type(s))

#Creation of set from string
name="Rama KRishna"
s=set(name)
print(s)
print(type(s))

#Creation of set from tuple
t=(10,20,30,40,50)
s=set(t)
print(s)
print(type(s))

#We cannot apply indexing and slicing in set.

#Applying membership operator in set
s={10,20,30,40,50}
print(30 in s)
print(60 not in s)

#Modification of set in python ---We can add or remove items from it.
#i.e., Set is mutable and its elements are immutable.

# initialize my_set 
my_set = {1, 3} 
print(my_set)
#my_set[0]
# if you uncomment the above line # you will get an error
# TypeError: 'set' object does not support indexing # add an element

#Add Method
# Output: {1, 2, 3} 
my_set.add(2) 
print(my_set)

#Update Method
# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4]) 
print(my_set)

# add list, set and tuple
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8},(9,10)) 
my_set.update(68,40) #it will not works it works only with itterable elements like list, tuple etc
print(my_set)

#another example
s={10}
l=[20,30]
t=(40,30,50)
s.update(l,t)
print(s)

s.update(l,range(10))
print(s)

#remove method
#It is used to remove the specified element from the set
#If the specified element is not present then it will raise Key Error
s={10,20,30,40,50}
s.remove(30)
print(s)

s={10,20,30,40,50}
s.remove(80)  # KeyError:80 
print(s)

#Discard Method
#It is exactly same as remove() but the difference is here if the specified element is not present then wont raise KeyError

s={10,20,30,40,50}
s.discard(80)  #no error
print(s)

#pop Method
#It is used to remove any random element fron the set, it the set is empty it will raised KeyError.
s={10,20,30,40,50}
s.pop() #print(s.pop()) --- It returns pop element
print(s)

#copy Method
#It is used to copy 
s1={10,20,30,40,50}
s2=s1.copy()
print(s1)
print(s2)
print(id(s1))
print(id(s2))

s1.add(80)
print(s1)
print(s2)

#Here also return same set of value but if we change the set elements in one set it will reflect another set also.
s1={10,20,30,40,50}
s2=s1  #assigning 
print(s1)
print(s2)
print(id(s1))
print(id(s2))

s1.add(80)
print(s1)
print(s2)

#clear method
#It is used to clear all then elements from the set
s1={10,20,30,40,50}
s1.clear()
print(s1)

'''Enumarate Function:
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
[(0, 'apple'), (1, 'banana'), (2, 'cherry')] '''







