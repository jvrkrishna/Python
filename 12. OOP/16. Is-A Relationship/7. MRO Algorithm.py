########## Method Resolution Order (MRO) Algorithm ##########
'''
This algorithm is used to solve the diamond problem in multiple inheritance or Hybrid Inheritance.
    
              A ---m1()
            *   *
          *       *
  m1()---B         C---m1()
          *       *
            *   *
              D---m1()

In the above structure we can understand that from where the m1 method can access.
1. First from D it takes.
2. In D not present it checks B and C Based on priority.
3. If not present in B and C then it checks A then object. (Here what is object).

Every class is a child of the built in object class, either directly or indirectly.
If we create a class without specifying any parent class, it automatically inherits from object.
'''
#Ex:
class Myclass:
    pass

print(issubclass(Myclass,object)) # True because Myclass is a subclass of object.

a=Myclass()
print(isinstance(a,object))  #True because a is an instance of object.

#Ex:
class Parent:
    pass
class Child(Parent):
    pass

print(issubclass(Parent,object))   #True
print(issubclass(Child,object))    #True
print(issubclass(Child,Parent))    #True

#The above diamond is very easy we can solve by seeing. Suppose if we have complex diamond then what we have to do. By following MRO Algorithm we can solve these type of Diamonds.

#MRO Algorithm:
'''
1. Consider the head element as first element.
2. Then check if the head is not available in the tail part of all other lists then add the head to the result.
else
Consider next list first element as the head element then do the same process until getting the result.

Ex:         Object          
              *
              A
            *   *
          *       *
        B           C
       *             *
     D                 E
     *                 *
       *             *
          *        *
            *    *
               F
MRO(A)=AO    MRO(B)=BAO    MRO(C)=CAO
MRO(D)=DBAO  MRO(E)=ECAO   MRO(F)=?     
'''

#Formula
'''MRO(?)=?+Merge([MRO(parent1)],[MRO(parent2)],....[Direct parent list])'''

#step 1: 
'''
MRO(F)=F+merge([MRO(D)],[MRO(E)],[DE])
      =F+merge([D BAO],[E CAO],[D E])--- Check the head element D with other lists tails
      =F+D+merge([B AO],[E CAO],[E])--- Check the head element B with other lists tails
      =F+D+B+merge([A O],[E CAO],[E])--- Check the head element A with other lists tails Here yes then next list E CAO is the next head element E then this E compares with last list in the last list there is no tail element the come in to result.
      =F+D+B+E+merge([A O],[C AO])--- Check the head element A with other lists tails
      =F+D+B+E+C+merge([A O],[A O])
      =F+D+B+E+C+A+merge([O],[O])
      =F+D+B+E+C+A+O
MRO(F)=F D B E C A O ----Retult
'''
#Example:
class A:pass
class B(A):pass
class C(A):pass
class D(B):pass
class E(C):pass
class F(D,E):pass

print(A.__mro__)
print(D.__mro__)
print(F.__mro__)

#Example:
class A:
    def m1(self):
        print("A of M1 method")
class B(A):pass
class C(A):pass
class D(B):pass
class E(C):pass
class F(D,E):pass

f=F()
f.m1()
print(F.__mro__)
