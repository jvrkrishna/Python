###Recursive Function
'''A function that calls by itself is known as recursive function.
Example:'''
def welcome():
    print("Hello Welcome to python")
    welcome()
    
welcome()

'''Example: Option to stop recursive function.'''
def sample():
    print("welcome to Janahita\n\n")
    print("press 1 to call function again \n")
    print("press 0 to exit\n")
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        sample()
    else:
        exit(0)
        
sample()

#WAP to print *'s using recursion
'''
*
**
***
****
*****
'''
def fun(num):
    print('*'*num)
    if num==5:
        return
    fun(num+1)

fun(1)

#WAP to print *'s using recursion
'''
*****
****
***
**
*
'''
def fun(num):
    print('*'*num)
    if num==1:
        return
    fun(num-1)

fun(5)

#WAP to print sum of natural numbers
'''
15
'''
def sum_of_n_numbers(n):
    if n<=1:
        return n
    else:
        return n+sum_of_n_numbers(n-1)
    
print(sum_of_n_numbers(5))

#Wap to print sum of fibbanocci series
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))