'''
Relationship is used to access the members of one class inside another class.
The advantage of relationships is code reusability.
There are two types of relationsships.
1. Has-A Relationship( also known as Composition)
2. IS-A Relationship( also known as Inheritance)
'''

#Examples:
'''
1. Employee HAS-A car
2. Employee IS-A Person
3. Car HAS-A Engine
4. Car IS-A Vehicle
'''

#1. HAS-A Relationship
'''
HAS-A Relationship is also known as Composition or Containership or Complex Objects.
In HAS-A Relationship we will build objects from smaller objects.
Ex: College is complex object and departments are smaller objects.

Here without College(Container Object) there are no departments(Contained objects).
'''

class Car:
    def __init__(self, cname, ccolor, cprice):
        self.cname = cname
        self.ccolor = ccolor
        self.cprice = cprice

    def Car_details(self,ename):
        print(f'{ename} Car Name is {self.cname}')
        print(f'{ename} Car color is {self.ccolor}')
        print(f'{ename} Car Price is {self.cprice}')
        print("* " * 20)


class Laptop:
    def __init__(self, lname, lcolor, lprice):
        self.lname = lname
        self.lcolor = lcolor
        self.lprice = lprice

    def Laptop_details(self, ename):  # Accept emp_name as an argument
        print(f'{ename} Laptop Name is {self.lname}')
        print(f'{ename} Laptop color is {self.lcolor}')
        print(f'{ename} Laptop Price is {self.lprice}')
        print("* " * 20)


class Person:
    def __init__(self, ename, eid, eaddress):
        self.ename = ename
        self.eid = eid
        self.eaddress = eaddress
        self.l = Laptop("Lenovo", "Grey", "40K")

    def Emp_details(self):
        print(f'Emp Name is {self.ename}')
        print(f'Emp ID is {self.eid}')
        print(f'Emp Address is {self.eaddress}')
        self.l.Laptop_details(self.ename)  # Pass the emp_name to the Laptop's details


# Example usage
p1 = Person("Sekhar", 1001, "Guntur")
p1.Emp_details()
        
'''
EEmp Name is Sekhar
Emp ID is 1001
Emp Address is Guntur
Sekhar Laptop Name is Lenovo
Sekhar Laptop color is Grey
Sekhar Laptop Price is 40K

'''

#Here in the above program Employee is Containership, car and laptops are smaller objects

