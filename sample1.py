class Parent:
    def m1(self):
        print('This is parent m1')
        
class Child(Parent):
    def m1(self):
        print('This is child m1')

c=Child()
c.m1()