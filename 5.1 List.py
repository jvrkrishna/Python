'''List a collection of elements with various data types. It is mutable mean we can change 
the values after creation of list also. List with [] brackets.'''

#Creation of a list
L1=[]
L1 = ["John", 102, 'USA',10,"20"]
L2 = [1, 2, 3, 4, 5, 6]
L3=list([1,"Ram"])
print(type(L1))
print(type(L2))
print(type(L3))
print(L1)

#Creation of list Dynamically by using eval() function.
L1=eval(input("Enter the L1 Elements:"))  #input ------ [10,20,30] ---- brackets compulsary
print(type(L1))
print(L1)

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

