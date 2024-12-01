#######Global Function
#Local variable has more scope than global variable. If we want to access global variable when local and global with same variable name the we use gobal function.
a=10
def sample():
    a=20
    print(a)   #20
    print(globals()['a'])   #10
sample()


####Nested fucntions
'''
Calling inner functions outside of outer function is not possible to call inner function outside of the function'''
def outer_fun():
    print("Inside outer function")
    def inner_fun():
        print('Inside inner function')
    inner_fun()
    
outer_fun()
#inner_fun() #error

#Example
def outer_fun():
    print("Inside outer function")
    def inner_fun():
        print('Inside inner function')
    return inner_fun
    
x=outer_fun() #when outer function is equal to some variable then it returns inner function as well
x() 
'''
Output:
Inside outer function
Inside inner function
'''