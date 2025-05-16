###########Armstrong number############
''' In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
'''
n = int(input("Enter n value: "))
sum = 0

# find the sum of the cube of each digit
temp = n
while temp > 0:
   digit = temp % 10
   sum =sum+ digit ** 3
   temp //= 10

# display the result
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
