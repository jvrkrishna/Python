#In Python, AST stands for Abstract Syntax Tree. It's a tree representation of the structure of Python source code. Python uses ASTs internally to understand and compile your code.

'''Why AST Is Useful
AST allows tools and programs to:
Analyze Python code.
Transform or generate Python code.
Perform static checks (like linters or type checkers).
Build custom compilers or interpreters.'''

#Example
import ast
code = "a = 2 + 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))
#Output (simplified):
'''
Module(
    body=[
        Assign(
            targets=[Name(id='a', ctx=Store())],
            value=BinOp(
                left=Constant(value=2),
                op=Add(),
                right=Constant(value=3)
            )
        )
    ]
)'''

#This output shows:
'''
An assignment to a.
The value is a binary operation: 2 + 3.

Useful AST Functions
ast.parse(source): Turns code into an AST.
ast.dump(node): Prints a representation of the AST.
ast.walk(tree): Iterate through nodes in the AST.
compile(ast_obj, filename, mode): Compile AST back into executable code.'''

#Example: Dynamic Typing for Dictionary Values
import ast

my_dict = {}

while True:
    key = input("Enter the key: ")
    value_input = input("Enter the value: ")

    try:
        # Safely evaluate value to its correct type (int, float, list, bool, etc.)
        value = ast.literal_eval(value_input)
    except (ValueError, SyntaxError):
        # Fallback: treat as a string if parsing fails
        value = value_input

    my_dict[key] = value

    choice = input("Do you want to add more elements to the dictionary? [Y/N]: ")
    if choice.upper() == 'N':
        break

print("Final dictionary:", my_dict)

#Example:Dynamic Typing for Only Integers and Strings
my_dict = {}

while True:
    key = input("Enter the key: ")
    value_input = input("Enter the value: ")

    # Check if the input is an integer
    if value_input.isdigit() or (value_input.startswith('-') and value_input[1:].isdigit()):
        value = int(value_input)
    else:
        value = value_input  # Treat anything else as a string

    my_dict[key] = value

    choice = input("Do you want to add more elements to the dictionary? [Y/N]: ")
    if choice.upper() == 'N':
        break

print("Final dictionary:", my_dict)

#Example: Accept Only int, list, tuple, or set
import ast

my_dict = {}

while True:
    key = input("Enter the key: ")
    value_input = input("Enter the value (int, list, tuple, or set): ")

    try:
        # Evaluate the input safely
        value = ast.literal_eval(value_input)

        # Check allowed types
        if not isinstance(value, (int, list, tuple, set)):
            raise ValueError("Only int, list, tuple, or set are allowed.")

    except (ValueError, SyntaxError) as e:
        print("Invalid input:", e)
        continue  # Skip and ask again

    my_dict[key] = value

    choice = input("Do you want to add more elements to the dictionary? [Y/N]: ")
    if choice.upper() == 'N':
        break

print("Final dictionary:", my_dict)