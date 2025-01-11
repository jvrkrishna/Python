#Strong Number
'''A Strong number is a special number whose sum of the all digit factorial should be equal to the number itself.For example - The given number is 145, we have to pick each digit and find the factorial 1! = 1, 4! = 24, and 5! = 120.'''
#Example:
number=input("Enter number : ")
sum=0
for i in number:
    fac=1
    for j in range (1,(int(i)+1)):
        fac=fac*j
    sum=sum+fac
    
if sum==int(number):
    print("This is strong number")
else:
    print("This is not a strong number")
