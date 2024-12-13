#Largest number among three numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b and a>c:
    print(f"The a value {a} is big")
elif b>c:
    print(f"The b value {b} is big")
else:
    print(f"The c value {c} is big")