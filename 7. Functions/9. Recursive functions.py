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
