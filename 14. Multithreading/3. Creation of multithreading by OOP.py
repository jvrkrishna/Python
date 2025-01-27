#Create thread in object oriented approach(Single thread)
class Test:
    def m1(self):
        for i in range(5):
            print("Ram")
    def m2(self):
        for i in range(5):
            print("Seetha")
obj=Test()
obj.m1()
obj.m2()

#By using multithreading
from threading import Thread
class Test:
    def m1(self):
        for i in range(5):
            print("Ram")
    def m2(self):
        for i in range(5):
            print("Seetha")
obj=Test()
t1=Thread(target=obj.m1)
t1.start()

t2=Thread(target=obj.m2)
t2.start()

#By using multithreading pass arguments
from threading import Thread
class Test:
    def m1(self,name):
        for i in range(5):
            print(name)
    def m2(self):
        for i in range(5):
            print("Seetha")
obj=Test()
t1=Thread(target=obj.m1,args=('Rama',))
t1.start()

t2=Thread(target=obj.m2)
t2.start()

