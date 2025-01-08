########## Hierarchical Inheritance ##########
'''
Multiple classes are derived from a single class.
'''
#Ex: A parent method have multiple childs that class B(A) and class C(A)
''' 
            class A
           *       *
         *           *
       *               *
    class B(A)      class C(A)
'''
#Example:
class A:
    def method1(self):
        print("Parent class method1")
class B(A):
    def method2(self):
        print("Child class method2")
class C(A):
    def method3(self):
        print("Child class method3")
b=B()
b.method1()
b.method2()

c=C()
c.method1()
c.method3 ()       
        
        