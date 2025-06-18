######## Process #######
'''
--->Program in execution is called as process.
--->When we are starting any application in our system at time, operating system will create process.
--->A process is an independent program with in its own memory space.
--->Ex: A person Notepad, MS word, browser then os will create 3 different process.
'''
######## Thread ########
'''
--->Thread is a smallest unit of a process or program.
--->A thread is an independent part with in a process.
--->A thread is a smaller unit of a process and shares the same memory space with other threads with in the process.
'''
###### Multitasking ######
'''
--->Doing multiple tasks in simultaneously called multitasking.
--->Generally multitasking are of 2 types.
    =>Thread based multitasking(Multiple tasks will execute with in a process, and each tasks are independent.)
    =>Process based multitasking(Multiple tasks will execute simultaneously, here each task are independent process.).
'''

###### Multithreading ########
'''
--->Multithreading is a technique, by using this technique we will break down a large task into multiple sub-tasks and execute these tasks simultaneously.
--->If we will use multithreading in our programming, then we will get better performance.
'''

##### Main Thread ####
'''
--->Whenever we are executing our python program then immediately PVM will send request OS to create one thread and that is MainThread.
--->By default, each python program will be executed by MainThread.
--->Each python program contain at least one thread that is MainThread.
If we want to work with thread in python, then we must import one inbuild module that is "threading".

How to know current working thread details.
print(threading.current_thread())
'''
#Example: Getting the information about current thread.
import threading
print(1)
print(2)
print(3)
print(threading.current_thread())

for i in range(5):
    print("Rk")
print(threading.current_thread())
print(threading.current_thread().name)  #thread name
print(threading.current_thread().ident) #thread id
print(threading.current_thread().is_alive()) #active or not