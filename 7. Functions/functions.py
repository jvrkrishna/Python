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

###Call By Value vs Call By reference

############ CALL BY VALUE ##################
'''If we made any chages on called function it will not reflect on outside the function when we call with value.'''

def sample(a):   #Called function
    print("Inside the function before Modification:",a)  #23
    print("Inside the function before Modification:",id(a))  #140706834615416
    a=100 #Here we cannot append because int is immutable.
    print("Inside the function after Modification:",a)  #100
    print("Inside the function after Modification:",id(a))  #140706834617880

a=23  #Here int is immutable
print("Outside the function before calling:",a)  #23
print("Outside the function before calling:",id(a))  #140706834615416
sample(a)  #Calling Function
print("Outside the function after calling:",a)  #23
print("Outside the function after calling:",id(a))  #140706834615416

############ CALL BY REFERENCE ##################
'''If we made any chages on called function it will reflect on outside the function when we call with reference.'''
def sample(a):   #Called function
    print("Inside the function before Modification:",a)  #[10, 20, 30]
    print("Inside the function before Modification:",id(a))  #2063865878784
    a.append(100)
    print("Inside the function before Modification:",a)  #[10, 20, 30, 100]
    print("Inside the function before Modification:",id(a))  #2063865878784

a=[10,20,30]  #Here list is mutable
print("Outside the function before calling:",a)  #[10, 20, 30]
print("Outside the function before calling:",id(a))  #2063865878784
sample(a)  #Calling Function
print("Outside the function after calling:",a)  #[10, 20, 30, 100]
print("Outside the function after calling:",id(a))  #2063865878784

###NOTE:
'''Python does not support Call by value or Call by reference it support by call by object reference. When we pass immutable objects like int,float, tuple it acts like call by value (i.e., modify that object and create new object.) and when we pass mutable objects like list, dictionary it acts like call by reference (i.e., modify that object and will not create new object.).'''