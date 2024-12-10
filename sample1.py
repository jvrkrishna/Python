#1. While Loop
#2. For Loop 

#WAP ro reap the numbers until -1 is entered also count the -ve, +ve and zero entered by users
no=int(input("Enter no value: "))
pn=0
nn=0
zn=0
while no!=-1:
    if no>0:
        pn=pn+1
    elif no<0:
        nn=nn+1
    else:
        zn=zn+1
    no=int(input("Enter no value:"))
else:
    print("Oh no is equal to -1")
    
print("Positive numbers: ",pn)
print("Negative numbers: ",nn)
print("Equal to zero numbers: ",zn)
