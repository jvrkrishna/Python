#Example:
def sample(a,b,c=30): #Here c is default argument
    print("Value of a is:",a,"The value of b is:",b,"The value of c is:",c)
sample(10,20)

#Example:
def sample(a,b,c=30): #Here c is default argument
    print("Value of a is:",a,"The value of b is:",b,"The value of c is:",c)
sample(10,20,40) #Here default argument modifies

#Example:
def sample(name,age=30): #Here age is default argument
    print(name,age)
sample(name="Rama Krishna")

#Example:
def sample(name,age=30): #Here age is default argument
    print(name,age)
sample(name="Rama Krishna") 
sample(age=25,name="Rama Krishna")
sample(25,"Rama Krishna")
