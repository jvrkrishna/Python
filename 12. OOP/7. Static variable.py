###Static variable
'''A variable that is shared across all instances of a class. It is class level variable.
If the value ot variable is fixed to all objects then we can go for static variable.'''
class Person:
    school_name="Sri chaitanya" #static variable
    def Details(self,name,age):
        self.name=name #instance variable
        self.age=age   #instance variable

print(Person.school_name)    #We can call directly by class
p1=Person()
print(p1.school_name) #we can call by object as well
