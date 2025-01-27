#Without multithreading program(Single thread)
def sample1():
    for i in range(3):
        print("Rama")
def sample2():
    for i in range(3):
        print("Seetha")
sample1()
sample2()

#In the above program when sample1 calls then process1 starts in that mainThread created. The MainThread is responsible for execute sample1 and same as for sample2 as well. Here same MainThread will execute sample1 and sample2 one after other.

#With multithreading program(Multi thread)
from threading import Thread
def sample1():
    for i in range(5):
        print("Rama")
def sample2():
    for i in range(5):
        print("Seetha")
#Creation of a thread
t1=Thread(target=sample1)
t1.start()

t2=Thread(target=sample2)
t2.start()

#Here in the above program there are three threads they are MainThread, t1 thread and t2 thread.
'''
Mainthread will going to execute below lines
from threading import Thread
t1=Thread(target=sample1)
t1.start()
t2=Thread(target=sample2)
t2.start()

t1 Thread will going to execute sample1()
t2 Thread will going to execute sample2()
'''

#Note: In the above program thread will executes parallel observe the output run multiple times the output changes the order every time.

# How to get Thread information
from threading import *
print('importing: ',current_thread().name)
def sample1():
    print('sample1(): ',current_thread().name)
    for i in range(5):
        print("Rama")
def sample2():
    print('sample2(): ',current_thread().name)
    for i in range(5):
        print("Seetha")
#Creation of a thread
t1=Thread(target=sample1)
t1.start()
print('t1.start(): ',current_thread().name)

t2=Thread(target=sample2)
t2.start()
print('t2.start(): ',current_thread().name)

'''
Output:
importing:  MainThread
sample1(): t1.start():   Thread-1 (sample1)MainThread
Rama
Ramasample2():
t2.start():  Rama Thread-2 (sample2)
MainThreadSeethaRama
RamaSeetha
Seetha
Seetha
Seetha
'''

# How to get thread count information
from threading import *
def sample1():
    for i in range(5):
        print("Rama")
def sample2():
    for i in range(5):
        print("Seetha")
#Creation of a thread
t1=Thread(target=sample1)
t1.start()
print("_Thread count:",active_count())

t2=Thread(target=sample2)
t2.start()
print("Thread count:",active_count())
