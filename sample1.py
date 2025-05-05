######### Calculator ##############
def add(a,b):
    return a+b
def sun(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("Please Choose the Below Options")
print("Press + to add, - to sub, * to Mul, / to Division")
choice=input("Enter the Choice:")
if choice=='+':
    print(f"The adding of {a} and {b} is{a+b}")
