#String is a collection of characters like(A-Z)(a-z)(0-9)(special symbols)
######Creation of a string #########
#Creation of a string by using '' or "" or ''' ''' or """ """

s1="Welcome to python Programming" #we can use '' or "" or ''' ''' or """ """
print(s1)

address="""          
#7-2,
Ramalay street,
Vinukonda,
Guntur,
Andhra pradesh"""  #we can use '' or "" or ''' ''' or """ """

print(address)

#Here we can take ' ' inside double quotes  or " " inside single quotes.
s1="Welcome to 'python' Programming"
s2='Welcome to "python" Programming'
print(s1)
print(s2)

#Doc string
def sample():
    """ The above
    line gives s1 data"""
    
    s1="hello world"
    return s1

print(sample.__doc__)   
print(sample())

#Another example
from random import randint
print(randint.__doc__)

#Accessing The elements of a string
#We can access elements of a string by using 1.Index 2.Slice Operator

#1.Index
#We can access the elements by positive and negative index as well.
s1="Welcome to python"
print(s1[3])
print(s1[7])
print(s1[8])
print(s1[-1])

#2.Slice Operator
#Slice represt a part of a string
s1="Welcome to python"
print(s1[1:5])
print(s1[0:10:2])
print(s1[::])
print(s1[::2])
print(s1[:8:2])

print(s1[-5:-1])
print(s1[-10:-1:2])
print(s1[::])
print(s1[::-2])
print(s1[:-8:-2])

#String Methods
s1="welcome to python"
print(s1.startswith("welcome"))
print(s1.startswith("Welcome"))
print(s1.endswith("python"))
print(s1.endswith("Python"))

print(s1.isalpha())
s2="Welcometopython"  #Without spaces then it is alpha
print(s2.isalpha())

s2="1Welcometopython"
print(s2.isalnum())

s3="1*2"
print(s3.isalnum())

s4="12"
print(s4.isdigit())

s5="1hello"
print(s5.islower())

s5="1HELLO"
print(s5.isupper())

s5="1Hello"  #Title meaning first letter should be capital
print(s5.istitle())

s5="1hEllo"  
print(s5.istitle())

s5="  "  
print(s5.isspace())


#Change Case Methods
s="Welcome to python"
print(s.upper())

print(s.lower())

print(s.swapcase())

print(s.title()) #Each word start with capital

# print(s.capitalize()) #First word will be in capital

#Length of a string
s1="Hello World"
print(len(s1))
print(s1.__len__())

#Count of a Character
s1="Hello World"
print(s1.count('o'))
print(s1.count('o',6)) #starts from 6th index

#replace a word
s1="Hello World"
print(s1.replace("World","Rk"))
print(s1) #original string cannot replace because it is immutable

#split Method
s1="Hello World"
print(s1.split())  #It returns a list
print(s1.split('o'))  #It split while 'o' comes

#Join Method
s1="Hello World"
print('*'.join(s1))    # H*e*l*l*o* *W*o*r*l*d

s1=["Hello", "World"]
print('*'.join(s1))    # Hello*World

s1=("Hello", "World")
print('.'.join(s1))    # Hello.World

#strip Method (Remove space from string)
s1="  Rama  "
print(len(s1))
print(len(s1.strip()))
print(s1.strip())

#Fill Method
s1="Rama"
print(s1.zfill(8))  #Here zfill is 8 and s1 is 4 then 8-4=4 it gives 4 zeros

#rjust method
s1="Rama"
print(s1.rjust(8))  #Here rjust is 8 and s1 is 4 then 8-4=4 it gives 4 spaces moves the s1 to right

s1="Rama"
print(s1.rjust(8, "*"))

s1="Rama"
print(s1.ljust(8, "*"))  # Rama****

#Center Method
s1="Rama"
print(s1.center(8))

s1="Rama"
print(s1.center(12,"*"))

#enumerate method
s1="Rama"
for i in enumerate(s1):
    print(i)