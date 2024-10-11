'''A tuple in Python is similar to a list. The difference between the two is that we 
cannot change the elements of a tuple once it is assigned whereas we can change the 
elements of a list. Tuple with () brackets.'''

#Creation of a Tuple
L1=()
L5=(20,) # , is mandatory otherwise it is trated as ordinary data type
L2 = ("John", 102, 'USA',10,"20")
L3 = (1, 2, 3, 4, 5, 6)
L4=tuple((1,"Ram")) #in this case we can use [],{}() ---inside brackets
print(type(L1))
print(type(L5))
print(type(L3))
print(type(L4))
print(L4)

#Creation of Tuple Dynamically by using eval() function.
L1=eval(input("Enter the L1 Elements:"))  #input ------ (10,20,30) ---- brackets compulsary
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
