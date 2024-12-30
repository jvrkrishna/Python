# Python program to swap two variables
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print(f'The value of x after swapping: {x}')
print(f'The value of y after swapping: {y}')

#Swap of two numbers Without Using Temporary Variable
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

