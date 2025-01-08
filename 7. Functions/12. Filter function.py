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
result=filter(sample,ages)
print(list(result))   # 1
for i in result:      #2   Either use 1 or 2 statement to print
    print(i)
    
#WAP to print age is greater than 18 by using filter with lambda function
ages=[10,20,30,40,5,8]
result=filter(lambda x:x>18,ages)
print(list(result))


#WAP to print the vowels is present in the specific elements with filter.
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

def fun(i):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (i in vowels):
        return True
    else:
        return False


Result = filter(fun, sequence)
print(list(Result)) 

#By using filter with lambda function
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
result=filter(lambda i:i in ['a', 'e', 'i', 'o', 'u'],sequence)
print(list(result))

#2nd way using filter with lambda function
print(list(filter(lambda i:i in ['a', 'e', 'i', 'o', 'u'],['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'])))

#3rd way using filter with lambda function
sequence = ['g', 'e', 'e', 'j', 'i', 'o', 'p', 'r']
vowels=['a', 'e', 'i', 'o', 'u']
result=filter(lambda i:i in vowels,sequence)
print(list(result))


#wap to print even items from dictionary
d={1:"Rama",2:"Krishna",3:"Gopal",4:"Rambabu"}
print(list(filter(lambda i:i[0]%2==0,d.items())))





