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
    
#Here in the above line of code we are writing the piece of code again and again on the scenarios use functions like below.
def Even_Odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        
Even_Odd(10)
Even_Odd(13)