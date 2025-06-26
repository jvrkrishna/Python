############### Class Method ######################
'''
Inside the class method we use static variables/ class-level variables.
The first argument of the class method is cls.
@classmethod decarator we have to write before class method.
we can call one class method inside the another class method.
Inside the class we can call class method using class name and outside the class we can call throught class name or object reference.
By using class method we can perform various operations like modify, delete, etc.
'''

#Example 1:
class person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def cls_method(cls):
        school_location="kakinada"
        print(f"My school name is {cls.school_name} and location is {school_location}")
    
person.cls_method() #we can call by class name
p1=person()
p1.cls_method() #we can call by object also


#Example 2:call class method inside another class method
class person:
    school_name="Sri Chaitanya"
    
    @classmethod
    def cls_method(cls):
        print(f"My school name is {cls.school_name}")
        person.another_cls_method()
        cls.another_cls_method()
        
    @classmethod
    def another_cls_method(cls):
        print(f"My school name is {cls.school_name}")
        
person.cls_method()

s1=person()
s1.cls_method()
s1.another_cls_method()


#Example 3: By using class method we can perform several operation to static variables.
class Test:
    a=10
    b=20
    
    @classmethod
    def access(cls):
        print(f"The value of a is {cls.a} and the value of b is {cls.b}")
    
    @classmethod
    def update(cls,x,y):
        cls.a=x
        cls.b=y

    @classmethod
    def delete(cls):
        del cls.a

Test.access()
Test.update(30,40)
Test.access()
Test.delete()
print(Test.__dict__)
