#Prime number:
'''If a number is divisible by 1 and itself is known as prime number 2,3,5,7,11,13'''
# num=int(input('Enter n value:'))
# # Negative numbers, 0 and 1 are not primes
# if num > 1:
  
#     # Iterate from 2 to n // 2
#     for i in range(2, (num//2)+1):
      
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

#prime number or not with in range
num=int(input('Enter n value:'))
start = 2
for i in range(start, num+1):
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count = 1
            break
    if count == 0:
        print(i)