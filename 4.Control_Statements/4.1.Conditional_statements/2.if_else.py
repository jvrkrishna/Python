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
    
# Write a program to print even or odd
num=int(input("Enter the number:"))
if num%2==0:
    print("The given number is Even")
else:
    print("The given number is odd")

#write a Program to check whether a person is eligible to vote or not.
age = int (input("Enter your age:"))
if age>=18:
    print("You are eligible to vote !!")
else:
    print("Sorry! you have to wait !!")

#sample program
user="ram"
passs="Ram@123"
user_name=input("Enter the User Name:")
password=input("Enter the Password:")
if user==user_name and passs==password:
    print("Success")
else:
    print("Try again")
    
'''A company decides to give bonus to its employee on this Dussehra.
A 5% bonus is given to the male workers and 10% bonus salary to the female workers
If the salary of the employee is less then 15000 then the employee get extra 3%
bonus on the salary
WAP to enter your salary and gender then calculate the bonus that has to given to the employee
and display the salary employee will get'''

salary=int(input("Enter the salary:"))
gender=input("Enter your gender:")

if gender=="m":
    bonus=0.05*salary
else:
    bonus=0.10*salary
    
if salary<=15000:
    bonus=bonus+0.03*salary
    
salary=bonus+salary

print("Salary is:",salary)
