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


##### return vs print
'''In functions internally return a value by default as None'''
#Example:
def add(a):
    print(a)

print(add(10))  #Here it will return None because we not returning any thing.  10  None

#Example
def add(a):
    print(a)
    return a-5

print(add(10))  #10  5

#Example
def add():
    list=[10,20,30]
    return list

print(add()) 

#Example:
def sample():
    print("Hello")

print(sample())   #Hello   None

#Example:
def sample():
    print("Hello")
    return 10

print(sample())   #Hello   10   #return replace None value

'''return statement only be at end of the function. If we give return statement in the middle after return statement remaining statement will not going to be executed.'''
#Python function can return multiple values.
def sample(a,b,c):
    return a,b,c

print(sample(10,20,30))


##### Types of Arguments #####
'''There may be several types of arguments which can be passed at the time of function calling.
•	Default arguments
•	Keyword arguments
•	Required or positional arguments
•	Variable-length arguments'''
 
#1. Positional Arguments:
'''Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.'''

#Example:
def sample(a,b,c):
    return a,b,c

print(sample(10,20)) #error because there are no sufficient required arguments on calling

#Example:
def sample(a,b):
    return "Name is:",a, "My age is:",b

print(sample(30, "Rama Krishna")) #These are not in correct position

#2. Keyword Arguments:
'''Python allows us to call the function with the keyword arguments. This kind of function call will enable us to pass the arguments in the random order.'''
#Example:
def sai(name,age,dep):
    print("Name:",name)
    print("Age:",age)
    print("Department:",dep)

sai("sairam",age=30,dep=120)

#Example:
def func(name1,message,name2):  
    print("printing the message with",name1,",",message,",and",name2)  
func("John",message="hello","David") #error positional argument follows keyword argument

#Positional argument cannot appear after keyword arguments

#Default arguments
'''While defining a function, we can initialize some of the arguments using default values. Passing default value to parameter is optional.
If we pass value to default argument, existing value will be replaced.'''

#Example:
def sample(a,b,c=30): #Here c is default argument
    print("Value of a is:",a,"The value of b is:",b,"The value of c is:",c)
sample(10,20)

#Example:
def sample(a,b,c=30): #Here c is default argument
    print("Value of a is:",a,"The value of b is:",b,"The value of c is:",c)
sample(10,20,40) #Here default argument modifies

#Example:
def sample(name,age=30): #Here age is default argument
    print(name,age)
sample(name="Rama Krishna")

#Example:
def sample(name,age=30): #Here age is default argument
    print(name,age)
sample(name="Rama Krishna") 
sample(age=25,name="Rama Krishna")
sample(25,"Rama Krishna")


###Variable-Length Arguments:
'''In the large projects, sometimes we may not know the number of arguments to be passed in advance. In such cases, Python provides us the flexibility to provide the comma separated values which are internally treated as tuples at the function call.
However, at the function definition, we have to define  *variable-name .
•	Non–Keyworded Arguments (*args)
•	Keyworded Arguments (**kwargs)'''

#Example:
def variableargs(a):
	print(a)
	
variableargs(10)

#Example:
def variableargs(a):
	print(a)
	
variableargs(10,20) # it gives an error because we declared one parameter but we passed two values.

#Example:
def variableargs(*a):
	print(a)
	
variableargs(10,35.2,"pyton") #it will executes because we take it is a pointer like tuple.
variableargs(name="Rama",age=24)#it gives an error beacue it is in dictinary format.

#Example:
def variableargs(**a):
	print(a)
variableargs(name="Rama",age=24)      #** accepts dictinary format.

#Example:
def variableargs(*a):
    print("Elements are:")
    for z in a:
        print(z)
 
variableargs(10,20,30,40)

#Example
def printme(*names):  
    print("type of passed argument is ",type(names))  
    print("printing the passed arguments...")  
    for name in names:  
        print(name)  
printme("john","David","smith","nick")  
'''Output:
type of passed argument is  <class 'tuple'>
printing the passed arguments...
john
David
smith
nick'''


# * and ** in function call

#Example:
def sample(a,b,c):
    print(a,b,c)

l=[10,20,30]  #This list a one element
sample(l)     #error sample() missing 2 required positional arguments: 'b' and 'c'

#Example:
def sample(a,b,c):
    print(a,b,c)
    
s={10,20,30}    
t=(10,20,30)
l=[10,20,30]
sample(*l)     # 10 20 30
sample(*s)     # 10 20 30
sample(*t)     # 10 20 30

#Example
def sample(**s):
    print(s)
    
d={'a':'10','b':'20','c':'30'}    
sample(**d)

