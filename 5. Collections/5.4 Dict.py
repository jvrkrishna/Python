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

#Accessing the dict elements
# get vs [] for retrieving elements 
my_dict = {'name': 'Jack', 'age': 26} 

# Output: Jack 
print(my_dict['name'])

# Output: 26 
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error # Output None
print(my_dict.get('address')) 

# KeyError 
print(my_dict['address'])

#Check whether key is existed or not
dict={1:"Rama",2:"Krishna"}
print(2 in dict)
print(3 not in dict)

#Create the dictionary Dynamically
dict={}

while True:
    key=input("Enter the Key :")
    value=input("Enter the value :")
    dict[key]=value
    
    choice=input("Enter the choice you want to add more elements in to dictionary [Y/N] :")
    
    if choice=='N':
        break

print(dict)

#Traversing List
dict={1:"Rama",2:"Krishna"}

for i in dict:
    print(i, dict[i])

#Add and Modify
dict={1:"Rama",2:"Krishna"}

dict[3]="Kat"
print(dict)

dict[1]="Ram"  #modify
print(dict)

#Delete
dict={1:"Rama",2:"Krishna"}

del dict[1]
print(dict)

del dict   #entire dictionary deleted 
print(dict)

#############Methods
#Get Method
#It is used to return the corresponding value associated with that key.
#If the specified key is not available then it will return the default value.
d={1:"Ram",2:"Krishna"}
print(d.get(1))
print(d.get(3))  #None
print(d.get(3, "Unknown")) #Unknown

#Items Method
d={1:"Ram",2:"Krishna"}
print(d.items())

for i in d.items():
    print(i)
    
for i, j in d.items():
    print(i,  j)

#pop Method
#It is used to remove the key and its associated value, then it will return that value.
#If the key is not available then it will raise KeyError.
#pop methods except one argumant if will not pass any argument then it will raise TypeError.
d={1:"Ram",2:"Krishna"}
d.pop(1)
print(d)
d.pop() #KeyError

d={1:"Ram",2:"Krishna"}
d.pop()

#popItem Method
#It is used to remove the last inserted item in Dictionary and return that item in tuple format
d={1:"Ram",2:"Krishna"}
print(d.popitem())

#Keys Method
#It is used to return all the keys of dictionary in list format.
d={1:"Ram",2:"Krishna"}
print(d.keys())

for i in d.keys():
    print(i)
    
#values Method
#It is used to return all the values of a dictionary in list format.
d={1:"Ram",2:"Krishna"}
print(d.values())

for i in d.values():
    print(i)

#setdefault Method
#Here as an argument we will provide key and value.
#It is used to return the value associated with that specified key.
#If the key is not available then key and value will be added as new item to the dictionary.
d={1:"Ram",2:"Krishna"}
print(d.setdefault(111, "Rama Krishna"))
print(d)

print(d.setdefault(2, 'Gopal')) #Key and value will not modified.
print(d)

#Update Mehtod
#It is used to add all the items d2 in d1.
d1={1:"Ram",2:"Krishna"}
d2={3:"Rama Krishna",4:"Gopal"}
d1.update(d2)
print(d1)

#If the key of both dict is same then it will be consider the updated one.
d1={1:"Ram",2:"Krishna"}
d2={2:"Rama Krishna",3:"Gopal"}
d1.update(d2)
print(d1)

#copy Method
#It is used to copy(Shallow Copy) all the item from one dict to another dict.
d1={1:"Ram",2:"Krishna"}
d2=d1.copy()
print(d1)
print(d2)
print(id(d1))   #112233
print(id(d2))   #112234

#Both dict are pointing to different memory locations so if we will made any changes on any particular dictionary it will not reflect to another dict.

d1={1:"Ram",2:"Krishna"}
d2=d1   #assign
print(d1)
print(d2)
print(id(d1))  #112233
print(id(d2))  #112233

#clear Method
#It is used to remove all the items of a dict but then our dict will become empty.
d1={1:"Ram",2:"Krishna"}
print(d1)
d1.clear()
print(d1)

#fromkeys Method
#It is used to create a new dict from given iterable(list, tuple, range etc) and value(it is optional)

l=[10,20,30]
d=dict.fromkeys(l)
print(d)

t=(10,20,30)
d=dict.fromkeys(t)
print(d)

r=range(5)
d=dict.fromkeys(r)
print(d)

r=range(5)
d=dict.fromkeys(r,"Hello")
print(d)

r=range(3)
l=["Ram","Banti","Chanti"]
d=dict.fromkeys(r, l)
print(d)


#Count the No of occurance present inside the string.
s="Rama"
d={}
for i in s:
    d[i]=d.get(i, 0)+1
print(d)

for i, j in d.items():
    print(f'{i} is present {j} times')
    
#Add the elements in to dictionary in run time
d={}
while True:
    name=input("Enter your name:")
    place=input("Enter your place:")
    d[name]=place
    choice=input("Do you want to add more candidates [Y/N]:")
    if choice=="N":
        break
    
#Access the elements from dictionary at run time
while True:
    name=input("Enter the name to get the place:")
    place=d.get(name)
    print(f"Hi {name} you are from {place}")
    
    choice=input("Do you want to search more[Y/N]:")
    
    if choice=="N":
        break

#Dictionary Comprehensions
d={i:i for i in range(0,5)}
print(d)
print(type(d))

d={i:i*i for i in range(0,5)}
print(d)
print(type(d))

l=[10,20,30,40]
d={i:3*i for i in l}
print(d)

name=["Rama", "Krishna","Gopal"]
d={i:len(i) for i in name}
print(d)

#Nested Dictionary
students={
1:{"name":"Rama Krishna","place":"Kakinada"},
2:{"name":"Rajaram","place":"rajahmundry"}
}

for i,j in students.items():
    print("student id is : ",i)
    
    for k in j:
        print(f"{k} is: {j[k]}")
    print('-'*20)

#Merging Dict Elements
d1={"Name":"Rama"}
d2={"Place":"Kakinada"}

d3={**d1, **d2}
print(d3)

