####### Multiple Inheritance ######
'''
. One class is derived from multiple classes.
. One child have multiple parents.
'''
#Ex: 
'''
       class A         Class B
              *       *
                *    *
                  * *
              class C(A,B)
'''

#Example: Multiple parents have one child class.
class A:
    def method1(self):
        print('A class method1')
class B:
    def method2(self):
        print('B class Method2')
class C(A,B):
    def method3(self):
        print('C class Method3')
    
c=C()
c.method1()
c.method2()
c.method3()

#Example: If both parents have same methods then which method is going to execute. It will execute based on priority.
class A:
    def method1(self):
        print('A class method')
class B:
    def method1(self):
        print('B class Method')
class C(A,B): #Here is the priority first A will execute.
    pass
    
c=C()
c.method1()


        
