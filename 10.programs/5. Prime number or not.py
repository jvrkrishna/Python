#Prime number:
'''If a number is divisible by 1 and itself is known as prime number 2,3,5,7,11,13'''
#Eg: 5 has factors of 1,5

n=int(input("Enter the number you want to know prime or not:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        # print(i)
        count+=1
# print("Count is:", count)
if count==2:
    print(f"The number {n} is a prime number.")
else:
    print(f"The number {n} is not a prime number.")
    
####WAP to print 1 to n prime numbers.
n=int(input("Enter the range you want to know prime or not:"))
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
    