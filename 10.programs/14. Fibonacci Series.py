'''The Fibonacci series starts with 0 and 1. Each number after that is the sum of the two numbers before it. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.'''

#for loop
a,b=0,1
n = int(input("Enter n value:"))

for i in range(n):
   print(a)
   a,b=b,a+b

#While Loop  
a,b=0,1  
n = int(input("Enter n value:"))

while b < n:
    print(a)
    a,b=b,a+b