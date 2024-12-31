while True:
    print("This is Loop")

while False:
    print("This is Loop")
else:
    print("Else")

a=int(input("Enter A Value:"))
while a<=30:
    print("Value of a is:",a)
    a=a+1       #a+=1

i=1
while i<=10:
    print(i)
    i+=1

# Write a program to print table
i=1
n=int(input("Enter n Value:"))
while i<=10:
    print("%d X %d = %d"%(n,i,n*i))  #print(f'{n} * {i} = {n*i}')
    i=i+1

#Using else with while loop
i=int(input("Enter n Value:"))
while i<=5:
    print(i)
    i=i+1
    if(i==3):
        break
else:print("The while loop exhausted")

#Using string print the characters
i=0
a="Rama krishna"
while i<len(a):
    if a[i]=='a':
        break 
    print(a[i])
    i=i+1

# WAP to print stars
i=1
while i<10:
    print("*",end=' ')
    i=i+1

#WAP to print sum of N natural numbers
i=1
sum=0
while i<10:
    sum=sum+i
    i=i+1
print("Sum is:",sum)


#WAP ro reap the numbers until -1 is entered also count the -ve, +ve and zero entered by users
num=int(input("Enter a value:"))
pn=0 #positive number
nn=0 #negative number
zn=0 #zero number
while num!=-1:
    if num>0:
        pn=pn+1
    elif num<0:
        nn=nn+1
    else:
        zn=zn+1
    num=int(input("Enter a value:"))

print("Number of positives",pn)
print("Number of Negatives",nn)
print("Number of Zeros",zn)
        
    
        