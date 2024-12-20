'''List a collection of elements with various data types. It is mutable mean we can change 
the values after creation of list also. List with [] brackets.'''
############################## 1. Creation #########################
#Creation of a list
L1=[]
L2 = ["John", 102, 'USA',10,"20"]
L4=list([1,"Ram"]) #in this case we can use [],{}() ---inside brackets
print(type(L1))
print(type(L2))
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

##################### 2. Access ############################
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
    
# Visiting the elements in a sequence and print the particular index
list=[30,40,50,"Ram",1,"Gopal",80]
for i in range(len(list)):
    if i==2:
        print(list[i])

list=[3,4,5,"Ram",1,"Gopal",8]
i=0
while i<len(list):
    if i==3:
        print(list[i])
    i=i+1

###WAP to display list elements of a list along with positive and negative index.###
list=[10,20,30]
n=len(list)
for i in range(n):
    print(f"{list[i]} is present at index {i}/{i-n}")
    
l2=[10,20,30]
n=len(l2)
z=0
for i in l2:
    print(f"{[i]} is in the index of {[z]}/{[z-n]}")
    z=z+1

list=[10,20,30]    
i=0
n=len(list)
while i<n:
    print(i, list[i],n-i)
    i=i+1
    
#########3. updating the list Elements###############
L1=[1,2,3,4,10,20,30]
L1[2]=30
print(L1)
L1[2:4]=30,40
print(L1)

#Update the list by using Iter method
L1=[1,2,3,4,10,20,30]
for i in range(3,6):
    #ele=int(input(f"Enter the {i} elements of the list:")) #for single element like 10
    ele=eval(input(f"Enter the {i} elements of the list:")) #for multi elements like 10,20
    L1.insert(i,ele)
print(L1)

################### Using methods on list ######################
####Append Method(Add at end)##Drawback we cannot add at Specified location-
list=[1,2,3]
list.append(4)  #To add as sub list use list.append([4])
print(list)

###Create a list by adding values Dynamically
list=[]
n=int(input("Enter the number of elements:"))
for k in range(0,n):
    ele=int(input(f"Enter the {k} element of the list:"))
    list.append(ele)  
    
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

#Update the list by using insert & Iter method
L1=[1,2,3,4,10,20,30]
for i in range(3,6):
    #ele=int(input(f"Enter the {i} elements of the list:")) #for single element like 10
    ele=eval(input(f"Enter the {i} elements of the list:")) #for multi elements like 10,20
    L1.insert(i,ele)
print(L1)

#######Count Method(Used to count how many times the element is present)
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1)) 

#####If we want to count multiple values then we go for iter
list=[10,20,30,40,10,30,56,45,10]
n=int(input("Enter the reqired element:"))
count=0
for i in range(len(list)):
    if list[i]==n:
        count=count+1

print(count)

######Index Method(Used to know the index number of specific element)
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

######index method by iter to know all indices
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
indices=[]
n=int(input("Enter the reqired element:"))
for i in range(len(List)):
    if List[i]==n:
        indices.append(i)
print(f"All indices of 10: {indices}")

#######pop Method used to delete element by index by default last element if we not mention index
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop()) #By default last element
print(List)

print(List.pop(3))
print(List) #By index number

#######pop using iter (Here iter is not useful it is directly popping the index but we can try)
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
n=int(input("Enter the reqired pop index:"))
for i in List:
    List.pop(n)
    break
print(f"Popped element: {n}")
print("Updated List:", List)

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

#creation of a list by using split()
a="Welcome to python world"
print(type(a))
print(a.split()) 
print(type(a.split()))


a="Welc-ome to pyt-hon wo-rld"
L2=a.split('-') # based up on('-') by default space
print(L2)

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

#########Copy Method
List = [8, 2, 3, 5,8,9]
print(List)
b=List.copy()
List.append(10)
print(List)
print(b)

###### Clear the complete list
List = [8, 2, 3, 5,8,9]
List.clear()
print(List)

####del Method used to delete specific element by index
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0] 
print(List)

#######Remove method(Used to Delete the specified element and by specific index element)
l1=[1,2,3,4,5,6,7,8,9,10,2]
l1.remove(2)    #l1.remove(l1[1])
print(l1)

list = [0,1,2,3,4]
print("printing original list: ")
for i in list:
    print(i,end=" ")

list.remove(2)
print("\nprinting the list after the removal of second element...") 

for i in list:
    print(i,end=" ")
    
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
        
#WAP to print the list of elements in reverse order      
list=[10,20,40,50,60]
n=len(list)-1

while n>=0:
    print(list[n])
    n=n-1
    
list=[10,20,40,50,60]
list.sort(reverse=True)
for i in list: 
    print(i)   
    
#WAP to print the elements in  sort order by using for or while
list=[10,50,30,40,20]
list.sort()
print(list)

list=[50,30,10,40,20]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
    print(list)
    
print("\nFinal List is:")
print(list)
    
 #WAP to print min and max values in the list
list=[10,30,4,50,35,60]
min=list[0]

for i in list:
    if i<min:
        min=i
        
print("Min is:", min)   

'''wap to search a value from a list then display its index, if the value is present
multiple times then print its all indices and also count the number of times that value 
is repeated in the list.'''

list=[10,20,30,40,50,10,20,30,40]
i=0
count=0
search=int(input("Enter the value you want to search:"))

while i<len(list):
    if search==list[i]:
        print(f"The value of {search} is present in the list and index is {i}")  
        count=count+1
    i=i+1
print(f'{search} is present {count} times')


###Example
l1={"Hi ", "Hello "}
l2={"Ram", "Banti","Seetha"}
new_list=[]

for i in l1:
    for j in l2:
        new_list.append(i+j)
        
print(new_list)  ###### Hi ram, Hi Banti, Hi seetha, Hello ram, Hello Banti, Hello Seetha

####Example to print first and last char in a word
l1={"Ram", "Banti","Seetha"}
new_list=[]

for i in l1:
        new_list.append(i[0]+i[-1])
        
print(new_list)

#enumerate function used to print the value and index
#By using enumerate the code will decrease.
l1=[10,20,30,40,50]

for i in enumerate(l1):
    print(i)
    
#If list is present inside another list is called as Nested List.
## 0  1   2  3  4[1,2,3]  5   6
l=[10,20,30,40,[41,42,43],50,60]
###Negative index as well

print(l[2])
print(l[4][1])


#Nested List in a Matrix
l=[[10,20,30],[40,50,60],[70,80,90]]

print(l)

####print row wise matrix
print(l[0])
print(l[1])
print(l[2])

for i in l:
    print(i)
    
#If you want to create a list from iterable objects like list,tuple,range,dict etc
#By writing very less code in efficient way then we can go for list comprehensions.
####Normal example
l=[]
for i in range(11):
    l.append(i)
    
print(l)

# ###By using list comprehension
l=[i for i in range(11)]
print(l)

l=[i*2 for i in range(11)]
print(l)


l=[i*i for i in range(11)]
print(l)

l=[i for i in range(1,21) if i%2==0]
print(l)

names=["ram","banti","Chanti"]
l=[i for i in names]
print(l)

names=["rama","banti","Chanti"]
l=[i[0:2] for i in names]
print(l)

#Create a list by add the elements which is containing letter a
names=["rama","banti","roji"]
l=[i for i in names if 'a' in i]
print(l)

#Replace the list element
names=["rama","banti","roji"]
l=[i if i !="banti" else 'hello' for i in names]
print(l)

#create alist form tuple
t=(10,20,30,40)
l=[i for i in t]
print(l)

#Create a matrcix using list comprehension
# m=[i for i in range(3)]  #Step 1
# print(m)

m=[[j for j in range(3)] for i in range(3)]
print(m)