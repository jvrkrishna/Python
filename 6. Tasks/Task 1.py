#WAP TO Take multiple inputs to single varaible
Name,Place=input("Enter Name, Place:").split(",")
print(f"My name is {Name.strip()} and I am from {Place}")

#Here from the above lines
#split() is used to sepate the input with comma(",")
#strip() is used to remove white spaces before and after the word.

#Wap To to give unlimited inputs in one line code.
list=[i for i in input("Enter the inputs:").split(",")]
print(list)

#Wap To to give limited inputs in one line code.
list=[input("Input:") for i in range(6)]
print(list)

#WAP to Print the single value as int.
d=int(input("Enter d value:"))
print(type(d))

#WAP to Print the multiple values as int.
a,b,c=map(int, input("Enter three values:").split())
print(type(a))