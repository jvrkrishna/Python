########### Hybrid Inheritance ###########
'''
Hybrid Inheritance is the collection of more than one inheritance.
'''
#Ex:
'''
single + multilevel
single + hierarchical
single + multiple
single + multilevel + hierarchical + multiple
'''

#Example:
class A:
    def method1(self):
        print("A class method1")
class B(A):
    def method2(self):
        print("B class method2")
class C(A):
    def method3(self):
        print("C class method3")  #Up to Here hierarchiccal Inheritance
class D(B,C):
    def method4(self):
        print("D class method4")  #This is multiple Inheritance

d=D()
d.method1()
d.method2()
d.method3()
d.method4()
        
    
