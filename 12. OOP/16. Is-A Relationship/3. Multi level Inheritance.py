##########Multi Level Inheritance ###########
'''
class is derived from a class and which is derived from another class.
'''
#Example:
#class A ------> class B(A) ------> class C(B)

#Example:
class A:
    def method1(self):
        print("This is parent A class Method1")
        
class B(A):
    def method2(self):
        print("This is child B class Method2")
    
class C(B):
    def method3(self):
        print("This is grandchild C class Method3")
        
a=A()
a.method1()

b=B()  
b.method1()
b.method2()

c=C()
c.method1()
c.method2()
c.method3()
