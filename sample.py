# #Creation of list Dynamically by using eval() function.
# l1=eval(input("Enter l1 Elements:"))
# print(l1)
# #Creation of list by using range() function.
# l2=list(range(1,10))
# print(l2)
#creation of a list by using split()
# l3="HIE TECH SOLUTIONS"
# a=l3.split()
# print(a)
#Accessing the elements from list
# l1=[10,20,30]
# print(l1[1])
#########updating the list Elements###############
# l1=[10,20,30]
# l1[1]=44
# print(l1)
########### Iterating the list for#################
# l1=[10,20,30]
# for i in l1:
#     print(i,l1)
########### Iterating the list while#################
# l2=[10,20,30]
# i=0
# while i<len(l2):
#     print(l2[i])
#     i=i+1
###WAP to display list elements of a list along with positive and negative index.###
# l2=[10,20,30]
# i=0
# while i<len(l2):
#     print(f"{l2[i]} is in the index of {[i]}/{[i-len(l2)]}")
#     i=i+1

l2=[10,20,30]
n=len(l2)
z=0
for i in l2:
    print(f"{[i]} is in the index of {[z]}/{[z-n]}")
    z=z+1
