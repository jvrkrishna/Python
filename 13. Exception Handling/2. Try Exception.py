'''In Python, an error occurs when something goes wrong during the execution of your code, causing it to fail or behave unexpectedly. Errors can arise due to syntax mistakes, invalid inputs, or other issues like division by zero or trying to access a non-existent file.

Python has different types of errors, and they can generally be categorized into two main groups:
1. Syntax Errors
2. Exceptions'''

#1. Syntax Errors:
'''These occur when Python cannot parse your code because it doesn’t follow the proper structure of the language.
For example, if you forget a colon after a function definition or misplace parentheses, you'll get a syntax error.

Below are the some of the Syntax errors.
1. Missing Colon (:)
Every control structure like if, for, while, and function definitions need a colon at the end of the line.

if x > 5
    print("x is greater than 5")
Error: SyntaxError: expected ':'

2. Mismatched Parentheses
Forgetting to close parentheses or mismatched opening and closing brackets can cause a syntax error.

print("Hello, World!"
Error: SyntaxError: unexpected EOF while parsing

3. Indentation Errors
Python relies on indentation to define code blocks. Incorrect indentation will lead to a syntax error.

def greet():
print("Hello!")  # IndentationError: expected an indented block

4. Missing Closing Quote for String
If you start a string with a quote but forget to close it, Python will raise a syntax error.

name = "Alice
print(name)
Error: SyntaxError: EOL while scanning string literal

5. Incorrect Function Definition
When defining a function, you need to use the correct syntax with parentheses.

def greet name:
print("Hello!")
Error: SyntaxError: invalid syntax

6. Using Reserved Keywords as Variable Names
You can't use Python's reserved keywords (like if, for, class, etc.) as variable names.

if = 10
Error: SyntaxError: invalid syntax

7. Unmatched Brackets or Braces
Forgetting to close a bracket or brace leads to a syntax error.

list = [1, 2, 3
Error: SyntaxError: unexpected EOF while parsing

8. Multiple Statements on One Line Without Semicolon
In Python, you can't have multiple statements on a single line without separating them with a semicolon.

x = 10 y = 20
Error: SyntaxError: invalid syntax

9. Using a Comma Instead of a Period
Accidentally using a comma instead of a period when accessing an attribute or method can cause a syntax error.

my_list = [1, 2, 3]
my_list.append, 4
Error: SyntaxError: invalid syntax

10. Invalid Function Call Syntax
Calling a function without parentheses or incorrectly formatting the function call can result in an error.

print "Hello"  # Missing parentheses
Error: SyntaxError: missing parentheses in call to 'print'

These are just a few examples. Syntax errors are usually easy to spot, as Python will give you a helpful error message pointing to the line where the issue is. 
'''

#2. Exceptions:
'''These occur while the program is running (during execution), and they usually indicate problems with the logic or environment.
Python has a variety of built-in exceptions, such as ZeroDivisionError, FileNotFoundError, IndexError, and TypeError.

Example (ZeroDivisionError):
a = 10 / 0
Error: ZeroDivisionError: division by zero

Example (FileNotFoundError):
with open('non_existent_file.txt', 'r') as file:
    content = file.read()
Error: FileNotFoundError: [Errno 2] No such file or directory

Common Python Errors
NameError: Occurs when you try to use a variable or function name that hasn’t been defined.
print(a)  # NameError: name 'a' is not defined

TypeError: Happens when an operation or function is applied to an object of inappropriate type.
print('5' + 5)  # TypeError: can only concatenate str (not "int") to str

ValueError: Raised when a function receives an argument of the right type but inappropriate value.
int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'

Handling Errors with Try and Except
Python provides a mechanism to handle errors gracefully using the try and except blocks. This allows you to catch and deal with exceptions without crashing your program.
''' 

#Exception:
'''
Exception is a runtime error.
Exception distrub normal flow of execution.
If exception will occur, then we can't exception normal execution or smooth execution.
Exception handling is a mechanism or technique or way to handle exception.
If exception handled successfully then we can except smooth termination.
It is highly recommended to handel the exception.
'''
#Handling Errors with Try and Except
#Example:
print('1')
print('2')
try:
    print(3/'3')
except Exception as e:
    print(e)
print('4') 

#Example:
l=[10,20,30]
try:
    print(l[6])
except Exception as e:
    print(e)

#Example: customised Exception message
l=[10,20,30]
try:
    print(l[6])
except Exception as e:
    print(e)
    print('The list index values we called is out of range') #Customised message
    
#Example exception of multiple errors
l=[10,20,30]
try:
    print(l[6])
    print(100/0)
except ZeroDivisionError as e:
    print(e)
except IndexError as I:
    print(I)

######### try except block #######
'''
--->Try block: Inside try block we will write critical/ dangerous/ risky code.
--->Except block: Inside except block we will write corresponding handling code.

Syntax:
try:
    #critical/ dangerous/ risky code
except Exception_Classname:
    #correponding handling code
'''

#System Define Exception
'''
Exception
   ||
   || Exception is the parent all errors
   ||
=>ZeroDivisionError
=>NameError
=>TypeError
=>IndexError
=>ValueError
=>KeyError
=>FileNotFoundError
=>ModuleNotFoundError
=>OverFlowError
=>IndentationError
'''

#ZeroDivision Error:
#Example: Handling error with Error Message
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
try:
    print(a/b)
except ZeroDivisionError:
    print(ZeroDivisionError)

'''
Output:
Enter a value:10
Enter b value:0
<class 'ZeroDivisionError'>
'''

#Example: Handling error with alternate handling code
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
try:
    print(a/b)  
except ZeroDivisionError:
    print(a+b)

'''
Output:
Enter a value:10
Enter b value:0
10
'''

#NameError
#Example: Handling error with Error Message
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
try:
    print(a+c)
except NameError:
    print(NameError)
    
'''
Output:
Enter a value:10
Enter b value:20
<class 'NameError'>
'''

#Example: Handling error with alternate handling code
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
try:
    print(a+c)
except NameError as e:
    print(e)
    
'''
Output:
Enter a value:10
Enter b value:20
name 'c' is not defined
'''

#TypeError
#Example: Handling error with Error Message
a=int(input("Enter a value:"))
b=input("Enter b value:")
try:
    result=a+b
except TypeError:
    print(TypeError)
    
'''
Enter a value:10
Enter b value:ram
<class 'TypeError'>
'''

#Example: Handling error with alternate handling code
a=int(input("Enter a value:"))
b=input("Enter b value:")
try:
    result=a+b
except TypeError as t:
    print(t)
     
'''
Output:
Enter a value:10
Enter b value:20
unsupported operand type(s) for +: 'int' and 'str'
'''

#Value Error
#Example: Handling error with Error Message
try:
    a=int(input("Enter a value:"))
    print(a)
except ValueError:
    print(ValueError)
    
'''
Enter a value:ram
<class 'ValueError'>
'''

#Example: Handling error with alternate handling code
try:
    a=int(input("Enter a value:"))
    print(a)
except ValueError as v:
    print(v)
     
'''
Output:
Enter a value:ram
invalid literal for int() with base 10: 'ram'
'''

#Index Error:
#Example:
l=[10,20,30,40]
print(l[8])
'''
Output:
IndexError: list index out of range
'''

#Example: Handling error with alternate handling code
l=[10,20,30,40]
try:
    print(l[int(input("Enter the list Index:"))])
except IndexError as I:
    print(I)

'''
Output:
Enter the list Index:8
list index out of range
'''

#Key Error:
#Example:
d={1:"Ram",2:"Seetha"}
print(d[3])
'''
Output:
KeyError: 3
'''

#Example: Handling error with alternate handling code
d={1:"Ram",2:"Seetha"}
try:
    print(d[3])
except KeyError as k:
    print(k)
'''
Output:
3
'''

#FileNotFound
try:
    f=open('abc.txt')
except FileNotFoundError as f:
    print(f)
'''
Output:
[Errno 2] No such file or directory: 'abc.txt'
'''

#ModuleNotFoundError
import pyqt5
'''
Output:
ModuleNotFoundError: No module named 'pyqt5'
'''

#OverFlowError
import math
print(math.factorial(64521354534534546))
'''
Output:
OverflowError: factorial() argument should not exceed 2147483647
'''

#IndentationError (We cannot handle it)
#It is a type of syntaxerror

