'''A tuple in Python is similar to a list. The difference between the two is that we 
cannot change the elements of a tuple once it is assigned whereas we can change the 
elements of a list. Tuple with () brackets.'''

###############1. Creation of tuple################
L1=()
L5=(20,) # , is mandatory otherwise it is treated as ordinary data type
L2 = ("John", 102, 'USA',10,"20")
L3 = (1, 2, 3, 4, 5, 6)
L4=tuple((1,"Ram")) #in this case we can use [],{}() ---inside brackets
print(type(L1))
print(type(L5))
print(type(L3))
print(type(L4))
print(L4)

#Creation of Tuple Dynamically by using eval() function.
L1=eval(input("Enter the L1 Elements:"))  #input ------ (10,20,30)
print(type(L1))
print(L1)

#Creation of tuple by using range() function.
L5=tuple(range(0,11))
print(type(L5))
print(L5)

#tuple can hold any complex data type like dict,tuple, etc
L1=(40,{"name":"Ram"},tuple((10,20,30)))
L1=40,{"name":"Ram"},"Raj",50 #tuple can create by using without brackets also
print(type(L1))
print(L1)

#creation of a tuple by using string 
a="Welcome to python world"
print(type(a))
L1=tuple(a) 
print(type(L1))
print(L1)


#####Accessing tuple Elements by positive and negative index
my_tuple = ('p','e','r','m','i','t') 
print(my_tuple[0]) # 'p' 
print(my_tuple[5]) # 't'

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) # nested index
print(n_tuple[0][3]) # 's'
print(n_tuple[1][1]) # 4

my_tuple = ('p', 'e', 'r', 'm', 'i', 't') 
print(my_tuple[-1])	# 't'
print(my_tuple[-6])	# 'p'

#Access the tuple by using slicing
print(my_tuple[::])

######## Modify tuple element ################
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9  # Output: (4, 2, 3, [9, 5]) 

#my_tuple[2]=4 Raise an error because tuple is immutable.
print(my_tuple)
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z') 
print(my_tuple)


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

'''We can use + operator to combine two tuples. This is called concatenation.
We can also repeat the elements in a tuple for a given number of times using the * operator.
Both + and * operations result in a new tuple.'''

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat') 
print(("Repeat",) * 3)

# traverse using for loop
t=(10,20,30,40,50)
for i in t:
    print(i)
    
# traverse using while loop
t=(10,20,30,40,50)
i=0
while i<len(t):
    print(t[i])
    i=i+1
    
# Deleting tuples
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z') # can't delete items

# TypeError: 'tuple' object doesn't support item deletion 
del my_tuple[3]

# Can delete an entire tuple 
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)

######### In built tuple methods ###########
# cmp(tuple1,tuple2)
t1=(50,60,70,80)
t2=(50,60,76,80)
print(t1==t2)
print(t1<t2)

# tuple(seq)
seq=[50,60,70,80]
result=tuple(seq)
print(result)

# len(tuple)
# max(tuple)
# min(tuple)

####### packing in tuple ###########
a=10
b=20
c=30
d=40
e="ram"
pack=a,b,c,d,e
print(pack)
print(type(pack))

####### un-packing in tuple ###########
pack=("Ram",10,20,30,40)
a,b,c,d,e=pack
print(a,b,c,d,e) #at the time of un-pack the no of variables and number of value must be same.

##### Tuple not support comprehension ########
