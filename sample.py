#WAP to print min and max values in the list
list=[10,30,4,50,35,60]
min=list[0]

for i in list:
    if i<min:
        min=i
        
print("Min is:", min)