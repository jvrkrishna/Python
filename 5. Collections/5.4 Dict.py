# #By using List, Tuple, Set we can store only values
# #Sometimes as a programmer we require to key and value as a pair in that case we can go to dictionary.

# # empty dictionary 
# my_dict = {}    #my_dict=dict()
# print(my_dict)

# # empty dictionary 
# my_dict = {}
# my_dict['name']="Rama"
# print(my_dict)

# # dictionary with integer keys 
# my_dict = {1: 'apple', 2: 'ball'}
# print(my_dict)
# print(my_dict[1])

# # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}
# print(my_dict)
# print(my_dict['name'])

# # using dict()
# my_dict = dict({1:'apple', 2:'ball'})
# print(my_dict)

# # from sequence having each item as a pair 
# my_dict = dict([(1,'apple'), (2,'ball')])
# print(my_dict)

# #Accessing the dict elements
# # get vs [] for retrieving elements 
# my_dict = {'name': 'Jack', 'age': 26} 

# # Output: Jack 
# print(my_dict['name'])

# # Output: 26 
# print(my_dict.get('age'))

# # Trying to access keys which doesn't exist throws error # Output None
# print(my_dict.get('address')) 

# # KeyError 
# print(my_dict['address'])

# #Check whether key is existed or not
# dict={1:"Rama",2:"Krishna"}
# print(2 in dict)
# print(3 not in dict)

# #Create the dictionary Dynamically
# dict={}

# while True:
#     key=input("Enter the Key :")
#     value=input("Enter the value :")
#     dict[key]=value
    
#     choice=input("Enter the choice you want to add more elements in to dictionary [Y/N] :")
    
#     if choice=='N':
#         break

# print(dict)

# #Traversing List
# dict={1:"Rama",2:"Krishna"}

# for i in dict:
#     print(i, dict[i])

# #Add and Modify
# dict={1:"Rama",2:"Krishna"}

# dict[3]="Kat"
# print(dict)

# dict[1]="Ram"  #modify
# print(dict)

# #Delete
# dict={1:"Rama",2:"Krishna"}

# del dict[1]
# print(dict)

# del dict   #entire dictionary deleted 
# print(dict)

# #############Methods
# #Get Method
# #It is used to return the corresponding value associated with that key.
# #If the specified key is not available then it will return the default value.
# d={1:"Ram",2:"Krishna"}
# print(d.get(1))
# print(d.get(3))  #None
# print(d.get(3, "Unknown")) #Unknown

# #Items Method
# d={1:"Ram",2:"Krishna"}
# print(d.items())

# for i in d.items():
#     print(i)
    
# for i, j in d.items():
#     print(i,  j)

# #pop Method
# #It is used to remove the key and its associated value, then it will return that value.
# #If the key is not available then it will raise KeyError.
# #pop methods except one argumant if will not pass any argument then it will raise TypeError.
# d={1:"Ram",2:"Krishna"}
# d.pop(1)
# print(d)
# d.pop() #KeyError

# d={1:"Ram",2:"Krishna"}
# d.pop()

# #popItem Method
# #It is used to remove the last inserted item in Dictionary and return that item in tuple format
# d={1:"Ram",2:"Krishna"}
# print(d.popitem())