# #Sum of Digits Ex: 123===== 1+2+3=6
# import math
# n=int(input("Enter n value:"))
# no=n
# sum=0
# while(n>0):
#     r=n%10
#     sum=sum+r
#     n=n/10
# #import math function to use trunc( ) function  trunc function is used to remove decimal values in python
# print(f"Sum of digits of {no} value is: {math.trunc(sum)}")

# #By using Loop
# n=input("Enter n value:")
# sum=0
# for i in n:
#     sum=sum+int(i)
# print(f"Sum of digits of {n} value is: {sum}")

#By using function
def sum_of_digits(n):
    sum=0
    for i in n:
        sum=sum+int(i)
    return sum_of_digits

n=input("Enter n value:")
print(sum_of_digits(n))

