class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Details(self):
        print('Person Information')
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
        print(30* '=')

#Creation of Mutiple Objects this method is some have difficult
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


#Creation of Mutiple Objects BY using Separate list and for Method 1
names=["Ram","Gopal"]
age=[30,25]

for i in range(len(names)):
    s=Student(names[i],age[i])
    s.Details()
    
#Creation of multiple objects by using lists and for and the output is stored in list.
obj_list=[]   
for i in range(len(names)):
    s=Student(names[i],age[i])
    obj_list.append(s)

for i in range(len(names)):
    print(obj_list[i].name)
    print(obj_list[i].age)
    
#Creation of Mutiple Objects By using Multi Elements single list and for Method 3.
students_list=[Student("Ram",30),Student("Gopal",25)]

for Student in students_list:
    Student.Details()


    
