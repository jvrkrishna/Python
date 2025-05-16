###########Reverse of a number#################
n=int(input("Enter n value:"))
reversed_num=0

while n != 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n//= 10

print("Reversed Number: " + str(reversed_num))

#Using slicing
n=int(input("Enter n value:"))
a=str(n)
print(a[::-1])

#Using for
n=int(input("Enter n value:"))
a=str(n)
ra=""
for i in range(len(a)):              
    ra=ra+a[len(a)-i-1]      
print(ra)

#Using for
n=int(input("Enter n value:"))
a=str(n)
ra=0
for i in range(len(a)):              
    digit = n % 10
    ra = ra * 10 + digit
    n //= 10   
print(ra)