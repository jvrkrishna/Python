'''
1. __name__ is a special variable.
2. If we want to know whether the program executed as a normal individual program or as a module then we use __name__ variable.
3. If you will execute a python individual program then it will give you the output as __main__.
4. If you will execute the program as a module from some other program then the value of __name__ variable is name of the module.
'''
#sample1.py
print("hello")
print(__name__)

#output
'''
hello
__main__  #it prints __main__ because it is directly execution
'''

#sample2.py
import sample1
print("hello")
print(__name__)

#Output:
'''
hello    #from sample1 program
sample1  #from sample1 program __name__ as module name because it imported
hello    #from sample2 program
__main__ #from sample2 program __name__ as __main__ because it is direct
'''

#Example:
#sample1 program code
def add(a,b):
    print(a+b)

if __name__=='__main__':
    add(10,20)
else:
    print("add() is not direct execution.")
    
'''If we run these above problem in sample1 it gives the output as 30'''

#sample 2 program code
import sample1

'''If we run the above code in sample2 it gives the output as 'add() is not direct execution.' '''
    