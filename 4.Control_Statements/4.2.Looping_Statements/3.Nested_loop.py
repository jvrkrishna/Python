# for i in range(1,11):
#     for j in range(2,4):
#         print(i*j,end = ' ')
#     print()


# n = int(input("Enter the number of rows you want to print?"))
# i,j=0,0
# for i in range(0,n):
#     print()
#     for j in range(0,i+1):
#         print("*",end=" ")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)



x = [1, 2]
y = [4, 5]
i = 0
while i < len(x) :
    j = 0
    while j < len(y) :
        print(x[i] , y[j])
        j = j + 1
    i = i + 1

