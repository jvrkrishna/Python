'''
Compound Interest
formula is
a=p*(1+r/100)T
where a is amount, p is principal amount, r is rate of interest and t is time in years
Now ci=a-p
'''


p=int(input("Enter principal amount:"))
t=float(input("Enter Time in years:"))
r=float(input("Enter rate of interest:"))
a=p*(1+r/100)**t   #a=p*pow(1+r/100,t)
ci=a-p
print("Compound Interest is:",ci)