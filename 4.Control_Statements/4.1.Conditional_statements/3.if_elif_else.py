if(5<2):
    print("this is if")
elif(5<2):
    print("this is elif")
else:
    print("this is else")


#write a program to to check the student grade.
marks = int(input("Enter the marks: "))
if marks > 85 and marks <= 100:
    print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
    print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
    print("You scored grade B ...")
elif (marks > 30 and marks <= 40):
    print("You scored grade C ...")
else:
    print("Sorry you are fail ?")
    
#Calculator program
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
print("press the \n + to add \n - to sub \n * to mul \n / to div")
choice=input("Enter your choice:")
if choice=='+':
    print(a+b)
elif choice=='-':
    print(a-b)
elif choice=="*":
    print(a*b)
elif choice=='/':
    print(a/b)
else:
    print("please select properly")

#Sample Program
'''Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''

# Solution:
n=int(input("Enter n value:").strip()) #Here strip() removes before and after spaces
if n%2 !=0:
    print("Weird")
elif n%2==0 and n in range(2,5):
    print("Not Weird")
elif n%2==0 and 6<n<=20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")