# Sum of factors of given number except itself is equals to the same number
# Ex: Suppose 6 factors are 1,2,3 then 1+2+3=6.
n=int(input('Enter n value:'))
Sum = 0
for j in range(1, n):
    if(n % j == 0):
        Sum = Sum + j
if (Sum == n):
    print("Number is a Perfect Number")
else:
    print("Number is not a Perfect Number")

#WAP to print perfect number in the range
n=int(input('Enter n value:'))
for i in range(1,n+1):
    Sum = 0
    for j in range(1, i):
        if(i % j == 0):
            Sum = Sum + j
    if (Sum == i):
        print(i)