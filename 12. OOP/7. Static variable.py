#static variables ----- A variable that is shared across all instances of a class. It is class level variable.If the value of variable is fixed to all objects then we can go for static variable.
'''
create
modify
access
del --- all these operation we can do in constructor, instance method, static method, class method, outside the class and inside the class.
'''

#Creation of static variable
class sample:
    a=10 #static inside the class
    def __init__(self):
        sample.b=20    #static inside the constrcutor 
            
    def m1(self):
        sample.c=30   #static inside the instance method
        
    @classmethod
    def m2(cls):
        sample.d=40 #static inside the classmethod
        
    @staticmethod
    def m3():
       sample.e=50 #static inside the static method
        
        
s=sample()
sample.f=60  #static inside outside the class

#Accessing of static variable
class sample:
    a=10 
    def __init__(self):
        sample.b=20    
            
    def m1(self):
        sample.c=30   
        
    @classmethod
    def m2(cls):
        sample.d=40
        
    @staticmethod
    def m3():
        sample.e=50 
        
        
s=sample()
sample.f=60 
print(sample.a) #accessing inside the class static variable by class
print(s.a) #accessing inside the class static variable by object

print(sample.b)
print(s.b)

s.m1()
print(sample.c)
print(s.c)

s.m2()
print(sample.d)
print(s.d)

s.m3()
print(sample.e)
print(s.e)

print(sample.f)
print(s.f)

#modification of static variable
class sample:
    a=10 
    print(f"a value in inside the class {a}")
    def __init__(self):
        sample.a=20  
        print(f"a value in constructor {sample.a}")  
            
    def m1(self):
        sample.a=30 
        print(f"a value in instance method {sample.a}")    
        
    @classmethod
    def m2(cls):
        sample.a=40
        print(f"a value in class method {sample.a}")  
        
    @staticmethod
    def m3():
        sample.a=50 
        print(f"a value in static method {sample.a}")  
        
        
s=sample()
sample.a=60 

sample.a
s.m1()
s.m2()
s.m3()

#Deleting of static variable
class sample:
    a=10 

    def __init__(self):
        del sample.a
            
    def m1(self):
        del sample.a
        
    @classmethod
    def m2(cls):
        del sample.a
        
    @staticmethod
    def m3():
        del sample.a 
       
s=sample()
del sample.a

print(sample.a)
