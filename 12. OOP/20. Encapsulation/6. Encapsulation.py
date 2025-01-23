##### Encapsulation ##########
'''
--->Encapsulation is a mechanism of wrapping the data and methods in to a single unit.
--->Prevents accidental modification or deletion.
--->In encapsulation:
    =>The attributes of a class will be hidden from other or outside classes.
    =>It can be access only by using methods of their current class.
''' 

#Accedental Modification
class College:
    def __init__(self):
        self.balance=50000
c=College()
print(c.balance) #Here any one can access
c.balance=100    #Here any one can modify
print(c.balance)
del c.balance    #Here any one can delete
print(c.balance)

#Prevention of Accedental Modification
class College:
    def __init__(self):
        self.__balance=50000 #data hiding --- private variable
c=College()
print(c.balance) #Here all cannot access 

#Encapsulation without authentication ---- Here accessing is possible but still we are not authorised user.
class College:
    def __init__(self):
        self.__balance=50000
    def getbalance(self):
        return self.__balance
c=College()
print(c.getbalance())

#Encapsulation with authentication ---- If we want to access we should provide authentication like password.
class College:
    def __init__(self):
        self.__balance=50000
    def getbalance(self,password):
        if password==2025:
            return self.__balance
        else:
            return "You are not authorised user"
c=College()
print(c.getbalance(2025))