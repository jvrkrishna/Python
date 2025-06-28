#Nested class
'''
. If a class is present inside the another class then this class is called an inner class.
. Inner class always depends upon outer class.
. If there is no outer class then there is no chance of inner class.
'''

class Outer:
    def __init__(self):
        print("Outer class")
    class Inner:
        def __init__(self):
            print("Inner class")
# #outer class object creation
o=Outer()

# #inner class object creation in different ways
i=o.Inner()
i1=Outer.Inner()
i2=Outer().Inner()

#object creation inside outer class
class Outer:
    def __init__(self):
        print("Outer class")
    class Inner:
        def __init__(self):
            print("Inner Class") 
    i=Inner()   
    
o=Outer() 
'''
Inner Class
Outer class
'''

#object creation Inner Inner class
class Outer:
    def __init__(self):
        print("Outer class")
    class Inner:
        def __init__(self):
            print("Inner Class") 
        class Inner1:
            def __init__(self):
                print("Inner in Class")  
    
o=Outer()
i=o.Inner()
i1=i.Inner1() 
'''
Outer class
Inner Class
Inner in Class
'''