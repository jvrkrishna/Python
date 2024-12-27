#Creation of Empty set is bit tricky

# s={}
# print(s)
# print(type(s))  #basically it is dictionary

#Here it will create empty dict. Instead of empty set.
#{} symbol is also used to create dict.
#We can create empty set by using set()

s=set()
print(s)
print(type(s))

#Creation of set with multiple elements:
s={10,20,(30,40),50}  #Set can hold only tuple elements cannot hold list,set or dict elements
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

#Creation of set from range()
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

#Union Method
#It is used to return all the elements presesnt in both the sets
s1={10,20,30,40}
s2={10,50,60}
print(s1.union(s2))
print(s1 | s2)

#Intersection Method
#It is used to return all the common elements in both the sets
s1={10,20,30,40}
s2={10,50,60}
print(s1.intersection(s2))
print(s1&s2)

#Difference Method
#It is used to return only a elements not S2 elements or not common elements
s1={10,20,30,40}
s2={10,50,60}
print(s1.difference(s2))
print(s1-s2)

#Symmetric Difference
#It is used to return all the elements which are in s1 and s2 but not common elements 
s1={10,20,30,40}
s2={10,50,60}
print(s1.symmetric_difference(s2))
print(s1^s2)

#Subset and Superset
A={1,2,3,4,5,6,7,8}
B={2,3,4}
print(B.issubset(A))
print(A.issuperset(B))

#Disjoint
A={1,2,3}
B={4,5}
print(A.isdisjoint(B))

#Set Comprehentions
#If you want to create a list from iterable objects like list,tuple,range,dict etc
#By writing very less code in efficient way then we can go for set comprehensions.
####Normal example
# s=set()
# for i in range(11):
#     s.add(i)
    
# print(s)

# # ###By using list comprehension
# s={i for i in range(11)}
# print(s)

# s={i*2 for i in range(11)}
# print(s)

#Another Example
# l=[10,20,30]
# s={i*i for i in l}
# print(s)

#Create a set by adding all the elements from 20 to 40 which is divisible by 4.
s={i for i in range(20,41) if i%4==0}
print(s)

#Create a set from list called as names by adding the first char of each element.
name=["Rama","Banti","Chanti"]
s={i for i in name}
print(s)

s={i[0] for i in name}
print(s)

s={i.upper() for i in name}
print(s)

#Create a set from a list(names) by adding all the elements but if the element is Rama then instead of Rama add Ram
names=["Raj","Rama","Raghu"]
s={i if i !='Rama' else 'Ram' for i in names}
print(s)

#Frozenset
#Frozenset is similar to set data structure but there is only the difference is frozenset is immutable in nature, so that we cant perform modification operation.
#Creation of Frozen Set
s={10,20,30,40}
fs=frozenset(s)
print(fs)
print(type(fs))

#Frozenset is immutable in nature so we cant use add(), remove() methods.
s={10,20,30,40}
fs=frozenset(s)
fs.add(26) #Error
fs.remove(20) #Error

#Merging set Elements
s1={10,20,30,40}
s2={50,"Rama"}
#s3=s1+s2 #It will not work in case of set
#print(s3)

s3={*s1, *s2}
print(s3)
