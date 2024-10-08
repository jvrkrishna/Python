if 5<2:
    print("this is if")
else:
    print("this is else")
    
# Write a program to print largest number
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b & a>c:
    print("a is big")
    
elif b>c:
    print("b is big")
    
else:
    print("c is big")

#write a Program to check whether a person is eligible to vote or not.
age = int (input("Enter your age:"))
if age>=18:
    print("You are eligible to vote !!")
else:
    print("Sorry! you have to wait !!")


user="ram"
passs="Ram@123"
user_name=input("Enter the User Name:")
password=input("Enter the Password:")
if user==user_name and passs==password:
    print("Success")
else:
    print("Try again")
