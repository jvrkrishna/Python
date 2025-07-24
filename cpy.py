#By using List, Tuple, Set we can store only values
#Sometimes as a programmer we require to key and value as a pair in that case we can go to dictionary.
#Dict is unordered, mutable and indexed by keys.

########Creating Dictionary
my_dict = {}    #my_dict=dict()
print(my_dict)

# adding a key value to empty dict
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
my_dict=dict([(1,"Apple"),(2,"Raju"),("Name","ravi")])
print(my_dict)

my_dict=dict(((1,"Apple"),(2,"Raju")))
print(my_dict)

my_dict=dict({(1,"Apple"),(2,"Raju")})
print(my_dict)

#####Create the dictionary dynamically
dict={}

while True:
    key=input("Enter the Key :")
    value=input("Enter the value :")
    dict[key]=value
    choice=input("Enter the choice you want to add more elements in to dictionary [Y/N] :")
    
    if choice=='N':
        break

print(dict)

############ Accessing the elements in the dict #############
my_dict={"name":"Rama","age":30}
print(my_dict["age"])

#We can try to access the key that not exist
print(my_dict["address"]) #Key Error

###Check whether key is existed or not#########
my_dict={"name":"Rama","age":30}
print("age" in my_dict)

##### Access the elements by using for loop
my_dict={1:"Rama",2:"Krishna"}

for i in my_dict:
    print(i, my_dict[i]) #keys= i and values=dict[i]'''

#######Modification
my_dict={1:"Rama",2:"Krishna"}

my_dict[1]="Gopal"  #Here we modify the values with the help of key not index number
print(my_dict)

my_dict[3]="Seetha" #We are adding elements to the dictionary
print(my_dict)

#########Delete a key value from dictionary
my_dict={1:"Rama",2:"Krishna"}

del my_dict[1]  #Here we deleted with the help of key not index
print(my_dict)

del dict   #entire dictionary deleted 
print(dict)

#############Methods###########
#Get method
'''
It is use to give the value corresponding to that key. If key is not present it returns None.'''
d={1:"ram",2:"Seetha"}
print(d.get(1))
print(d.get(3))

print(d.get(3, "Please check the key is present or not"))

#items method
'''Item return the complete items in the dictionary both key and values'''
d={1:"ram",2:"Seetha"}
print(d.items())

for i in d.items():
    print(i)

#Keys method
''' It returns the keys only'''
d={1:"ram",2:"Seetha"}
print(d.keys())

for i in d.keys():
    print(i)
 
#Values method
''' It returns the values only'''  
d={1:"ram",2:"Seetha"}
print(d.values()) 

for i in d.values():
    print(i)
    
#pop method
'''It is used to remove the key and value. If the key is not present then it will raise KeyError.'''
d={1:"ram",2:"Seetha"}
d.pop(1)  #Here we have to pass atleast one key. If no key is passed it raise error.
print(d)

#pop Item Method
''' It is used to remove the last inserted item in dict'''
d={1:"ram",2:"Seetha"}
d.popitem()
print(d)

#Set Default method
'''Here an argument we will provide key and value. It is used to return the value with that key. If the key is not present then the value will be added as new item to dictionary.'''
d={1:"ram",2:"Seetha"}
print(d.setdefault(11, "Rama Krishna"))
print(d)

print(d.setdefault(2, "Harini"))
print(d)

#Update Method
'''It is used to add all the elements from one dict to another dict.'''
d1={1:"ram",2:"Seetha"}
d2={3:"Raju",4:"Harini"}
d1.update(d2)
print(d1)

#If the key is present in both dict then it will be consider the updated one
d1={1:"ram",2:"Seetha"}
d2={2:"Raju",4:"Harini"}
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
    key=input("Enter the Key:")
    value=input("Enter the Value:")
    d[key]=value
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

