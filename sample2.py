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