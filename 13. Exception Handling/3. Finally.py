######### Finally Block ##########
'''
-->Inside finally block we will write clean-up code.
-->Clean-up codes are the must executes codes.
-->Finally is the best option to write the cleanup code.
-->Finally is a block and it will execute every time, it does not matter whether exception raised or not raised, exception handle or not.

Syntax:
try:
    #critical code
except exception_classname:
    #corresponding handling code
finally:
    #clean-up code
'''

#Example:
try:
    print("File Opening code")
except Exception as e:
    print(e)
finally:          #Mandatory Execution
    print("File Closing mode")
'''
Output:
File Opening code
File Closing mode
'''

#Example:
try:
    print(10/0)
except Exception as e:
    print(e)
finally:     #mandatory Execution
    print("Finally Code executed")
'''
Output:
division by zero
Finally Code executed
'''

#Example:
try:
    print(10/0)
except FileNotFoundError as f:   #This is different exception not ZeroDivisionError.
    print(f)
finally:     #In this case finally block executes first
    print("Finally Code executed")
'''
Output:
Finally Code executed
ZeroDivisionError: division by zero
'''

#Example:
try:
    print(1)
    print(2)
    print("File open code")
    print(4)
    print(10/0)
    print("File close code") #dont write clean-up code inside the try block because it can't execute
except FileNotFoundError as e:
    print(e)
finally:
    print("Finally Block executed")

'''
output:
1
2
File open code
4
Finally Block executed
ZeroDivisionError: division by zero
'''

#Example:
try:
    print(1)
    print(2)
    print("File open code")
    print(4)
    print(10/0)
except FileNotFoundError as e:
    print(e)
finally:
    print("File close code") #Write the clean up code in finally block because it is mandatory execution.

'''
output:
1
2
File open code
4
File close code
ZeroDivisionError: division by zero
'''

#Is there any situation where finally won't be executed.
'''
-->If we will forcefully shutdown PVM.
-->Inside function if we will write finally block after return statement(Which is false statement).
'''

#Example: If we forcefully shutdown the PVM then finally block not executed.
import os
try:
    print(1)
    print("file open code")
    os._exit(0)   #Code to shutdown PVM
    print(3)
except Exception as e:
    print(e)
finally:
    print("Finally block")
'''
Output:
1
file open code
'''

#Example:finally with funcction return statement
def sample():
    try:
        print(1)
        return "Hello"
        print(3)
    except Exception as e:
        print(e)
    finally:
        print('Finally block executed') #Here finally block is executed
print(sample())
'''
Output:
1
Finally block executed
Hello
'''
