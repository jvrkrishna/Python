# Sum of factors of given number except itself is equals to the same number
# Ex: Suppose 6 factors are 1,2,3 then 1+2+3=6.
n=int(input("Enter the number you want to know perfect or not:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print(f"The number {n} is a perfect number.")
else:
    print(f"The number {n} is not a perfect number.")

####WAP to print 1 to n perfect numbers.
n=int(input('Enter n value:'))
for i in range(1,n+1):
    Sum = 0
    for j in range(1, i):
        if(i % j == 0):
            Sum = Sum + j
    if (Sum == i):
        print(i)