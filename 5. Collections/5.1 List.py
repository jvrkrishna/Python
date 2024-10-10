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

#Accessing the elements from list
list = [1,2,3,4,5,6,7]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# Accessing the elements by using slice operator
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

#########updating the list Elements###############
L1=[1,2,3,4,10,20,30]
L1[2]=30
print(L1)
L1[2:4]=30,40
print(L1)

########### Iterating the list#################
#Visiting all the elements in a sequence is called Traversing
list = ["John", "David", "James", "Jonathan"]
for i in list:
    print(i)
    
list = ["John", "David", "James", "Jonathan"]
i=0
while i<len(list):
    print(list[i])
    i=i+1
    
###WAP to display list elements of a list along with positive and negative index.###
list=[10,20,30]
n=len(list)
for i in range(n):
    print(f"{list[i]} is present at index {i}/{i-n}")
    
################### Using methods on list ######################
#####Append Method(Add at end)##Drawback we cannot add at Specified loction-
list=[1,2,3]
list.append(4)  #To add as sub list use list.append([4])
print(list)

###Create a list by adding 20 0s in list
l=[]
for i in range(20):
    l.append(0)
    
print(l)

#####Insert Method(Insert the element at specified location)
l1=[1,2,3,4,2,5,6,7,2,8,9,10]
l1.insert(3,24)    #3rd index value 24
print(l1)

l1.insert(20,84)  #insert at end because there are no such indexes
print(l1)
l1.insert(-34,88) #insert at start because there are no such indexes
print(l1)

#######Count Method(Used to count how many times the element is present)
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1)) 

######Index Method(Used to know the index number of specific element)
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

#######Remove method(Used to Delete the specified element)
l1=[1,2,3,4,5,6,7,8,9,10]
l1.remove(l1[2])
print(l1)

list = [0,1,2,3,4]
print("printing original list: ");
for i in list:
    print(i,end=" ")

list.remove(2)
print("\nprinting the list after the removal of second element...") 

for i in list:
    print(i,end=" ")

#######pop Method used to delete element by index by default last element if we not mention index
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop()) #By default last element
print(List)

print(List.pop(3))
print(List) #By index number

#######extend method (Used to extend the list or add a sublist)
list=[1,2,3]
list.extend([4])  #we cannot process this extend as sublist
print(list)


List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]

# Add List2 to List1
List1.extend(List2)
print(List1)
# now Add List1 to List2 List2.extend(List1) 
print(List2)


######Sum Method
List = [1, 2, 3, 4, 5]
print(sum(List)) 

######Length Method
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List)) 

list=[1,3,2,5,2,7,8]
for i in range(len(list)):
    if list[i]==2:
        print(i)

###### Min method
List = [8, 2, 3, 5,8,9]
print(min(List))

###### Clear the complete list
List = [8, 2, 3, 5,8,9]
List.clear()
print(List)


#########Copy Method
List = [8, 2, 3, 5,8,9]
print(List)
b=List.copy()
List.append(10)
print(List)
print(b)


####del Method used to delete specific element by index
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0] 
print(List)

####remove Method used to delete specific element by element
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3) 
print(List) 

##### reverse method It is used to reverse the list.
List = [8, 2, 3, 5,8,9]
List.reverse()
print(List)


######sort() It is used to sort the order.
list = [8, 2, 3, 5,8,9]
list.sort()
print(list)

list.sort(reverse=True)  #Decending order
print(list)

#Concatination of list
L1=[20,30,40,50,60]
S1=['Ram','Priyanka',40,50]
C1=L1+S1
print(C1)

#Repetition of Lists
L1=[10,20,40]
Rep=L1*5
print(Rep)

#WAP to check the number is present in the list or not until it matches
L1=[10,20,30,40,50,60]
choice=int(input("Enter your Lucky Number:"))
while True:
    if choice in L1:
        print("Yes your number is present")
        break
    else:
        print("The number is not present")
        choice=int(input("Enter your Lucky Number:"))
        
        
    
