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


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print('Person Information')
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(30* '=')

#Creation of Mutiple Objects By using list and for
students_list=[Student("Ram",30),Student("Gopal",25)]

for Student in students_list:
    Student.Details()
    
#Creation of Mutiple Objects BY using list and for
names=["Ram","Gopal"]
age=[30,25]

for i in range(len(names)):
    s=Student(names[i],age[i])


