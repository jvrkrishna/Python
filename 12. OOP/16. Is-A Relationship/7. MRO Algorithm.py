########## MRO Algorithm ##########
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

