#Functions is the collection of statements or a piece of code to perform a specific task.
###Advantages###
'''
Code Reusability
Improve Modularity
'''

#Types of Fucntions
'''
1. Build in Functions
2. User Defined Functions.
'''

#1. Build in Functions:
'''These Functions are already created by python people such type of functions are called as predefined functions or Build in functions.
Ex: print(), min(), max(), input(), etc...'''

#2. User Defined Functions.
'''These functions are created by user as per requirement. 
Ex: display(), add(), greetings(), etc...'''

#####Use of Functions
'''If we want to execute a piece of code for multiple times then we go for functions.'''

a=10
if a%2==0:
    print('Even')
else:
    print('odd')
    
b=20
if b%2==0:
    print('Even')
else:
    print('odd')
    
c=30
if c%2==0:
    print('Even')
else:
    print('odd')
    
#Here in the above line of code we are writing the piece of code again and again on the scenarios uuse functions like below.
def Even_Odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        
Even_Odd(10)
Even_Odd(13)

###Parameter vs arguments
''' Parameters is just like variable present inside the function while defining'''
def add(a,b):     # parameters / Formal arguments
    print(a+b)
    
add(10,20)   # arguments / actual arguments