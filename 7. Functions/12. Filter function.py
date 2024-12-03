'''The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.'''

#syntax:
'''filter(function, sequence)'''
#function: 
'''function that tests if each element of a sequence true or not.'''
#sequence:
'''sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.'''

#Note: Filter gives the true output only.

#Example:
ages=[10,20,30,4,5,9]

def sample(x):
    if x>18:
        return True
    else:
        return False
adults=filter(sample,ages)

# 1
print(list(adults))

#2   Either use 1 or 2 statement to print
for i in adults:
    print(i)
    
#WAP to print age is greater than 18 by using filter with lambda function
ages=[10,20,30,40,5,8]

adults=filter(lambda x:x>18,ages)
print(list(adults))