'''The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.'''

#syntax:
'''filter(function, sequence)'''
#function: 
'''function that tests if each element of a sequence true or not.'''
#sequence:
'''sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.'''

#Note: Filter gives the true output only.

#WAP to print age is greater than 18 by using filter
ages=[10,20,30,4,5,9]

def sample(x):
    if x>18:
        return True
    else:
        return False
adults=filter(sample,ages)
print(list(adults))   # 1
for i in adults:      #2   Either use 1 or 2 statement to print
    print(i)
    
#WAP to print age is greater than 18 by using filter with lambda function
ages=[10,20,30,40,5,8]
adults=filter(lambda x:x>18,ages)
print(list(adults))


#WAP to print the vowels is present in the specific elements with filter.
def fun(i):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (i in letters):
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)
print('The filtered letters are:') 
print(list(filtered)) 

#By using filter with lambda function
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
output=filter(lambda i:i in ['a', 'e', 'i', 'o', 'u'],sequence)
print(list(output))

#2nd way using filter with lambda function
print(list(filter(lambda i:i in ['a', 'e', 'i', 'o', 'u'],['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'])))

#3rd way using filter with lambda function
sequence = ['g', 'e', 'e', 'j', 'i', 'o', 'p', 'r']
vowels=['a', 'e', 'i', 'o', 'u']
output=filter(lambda i:i in vowels,sequence)
print(list(output))


#wap to print even items from dictionary
d={1:"Rama",2:"Krishna",3:"Gopal",4:"Rambabu"}
print(list(filter(lambda i:i[0]%2==0,d.items())))