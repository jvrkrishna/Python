#Sum of Digits Ex: 123===== 1+2+3=6
import math
n=int(input("Enter n value:"))
no=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r
    n=n/10
#import math function to use trunc( ) function  trunc function is used to remove decimal values in python
print(f"Sum of digits of {no} value is: {math.trunc(sum)}")