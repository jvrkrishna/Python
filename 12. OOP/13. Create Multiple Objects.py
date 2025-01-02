class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print('Person Information')
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(30* '=')

#Creation of Mutiple Objects
s1=Student("Ram",30)
s1.Details()

s2=Student("Gopi",25)
s2.Details()

s3=Student("Raju",32)
s3.Details()
