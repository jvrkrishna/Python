#Largest number among three numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b and a>c:
    print(f"The value of {a} is big")
elif b>c:
    print(f"The value of {b} is big")
else:
    print(f"The value of {c} is big")