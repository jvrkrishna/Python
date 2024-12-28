# i=1
# while(i<=3):
#     print(i)
#     j=1
#     while(j<=3):
#         print(j)
#         j=j+1
#     i=i+1
    
# i=1
# while(i<=3):
#     print("Ram")
#     j=1
#     while(j<=3):
#         print("Seetha")
#         j=j+1
#     i=i+1



# x = [1, 2]
# y = [4, 5]
# i = 0
# while i < len(x) :
#     j = 0
#     while j < len(y) :
#         print(x[i] , y[j])
#         j = j + 1
#     i = i + 1



# for i in range(1,11):
#     for j in range(2,4):
#         print(i*j,end = ' ')
#     print()


# n = int(input("Enter the number of rows you want to print?"))
# i,j=0,0
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)

#WAP to print the numbers as below output format
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5  
'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#WAP to print the numbers as below output format
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    




