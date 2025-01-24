##### Else Block ####
'''
-->If there is no exception in try block then else block will be executed.
Syntax:
try:
    #Critical code
except Exception_ClassName:
    #Corresponding handling code
else:
    #write the code if there is not exception
finally:
    #clean-up code
'''

#Example: try except else finally
try:
    print(10/0) #Here Exception is there so else block will not execute.
except ZeroDivisionError as z:
    print(z)
else:
    print("I am else block")

'''
Output:
division by zero
'''

#Example:
try:
    print(10/2) #Here Exception is not there so finally block executed.
except ZeroDivisionError as z:
    print(z)
else:
    print("I am else block")
    
'''
Output:
5.0
I am else block
'''

#Example:
def add(a,b):
    try:
        result=a+b
    except Exception as e:
        print(e)
    else:
        print(f"The result is:{result}")
add(int(input("Enter a value:")),int(input("Enter b value:")))

'''
Output:
Enter a value:10
Enter b value:Ram
ValueError: invalid literal for int() with base 10: 'Ram'
'''

#Example:
def add(a,b):
    try:
        result=a+b
    except Exception as e:
        print(e)
    else:
        print(f"The result is:{result}")
add(int(input("Enter a value:")),int(input("Enter b value:")))

'''
Output:
Enter a value:10
Enter b value:20
The result is:30
'''