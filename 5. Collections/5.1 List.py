'''List a collection of elements with various data types. It is mutable mean we can change 
the values after creation of list also. List with [] brackets.'''

#Creation of a list
L1=[]
L2 = ["John", 102, 'USA',10,"20"]
L3 = [1, 2, 3, 4, 5, 6]
L4=list([1,"Ram"]) #in this case we can use [],{}() ---inside brackets
print(type(L1))
print(type(L2))
print(type(L3))
print(L1)

#Creation of list Dynamically by using eval() function.
L1=eval(input("Enter the L1 Elements:"))  #input ------ [10,20,30] ---- brackets compulsary
print(type(L1))
print(L1)

#Creation of list by using range() function.
L5=list(range(0,11))
print(type(L5))
print(L5)

#List can hold any complex data type like dict,tuple, etc
L1=[40,{"name":"Ram"},list((10,20,30))]
print(type(L1))
print(L1)

#creation of a list by using split()
a="Welcome to python world"
print(type(a))
L1=a.split() 
print(type(L1))
print(L1)

a="Welc-ome to pyt-hon wo-rld"
L2=a.split('-') # based up on('-') by default space
print(L2)


list = [1,2,3,4,5,6,7]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# Slicing the elements
print(list[0:6])
print(list[:])
print(list[2:5])
print(list[2:5+1])
print(list[1:6:2])
print(list[-1])

list2 = [1,2,3,4,5]
print(list2[-1])
print(list2[-3:])
print(list2[:-1])
print(list2[-3:-1])

