#########WAP to print uppere half diamond
'''
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
'''

#Example:
n=6
for i in range(1,n):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#WAP to print Lower diamond pattern
'''
 1 2 3 4 
  1 2 3 
   1 2 
    1 
'''
n=6
for i in range(n-2,0,-1):
    print(" "*(n-i),end="") #print leading spaces
    for j in range(1,i+1):
        print(j,end=" ") #print numbers with spaces
    print()

