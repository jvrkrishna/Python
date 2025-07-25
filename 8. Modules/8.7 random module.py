# Random Number
'''Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:'''

#If we want to generate random values then we use random module.
import random

#randint() it will generate random int values 
print(random.randint(1,10))  #We are included both 1 and 10.

#random() it will generate random float values
print(random.random())

#randrange()   
print(random.randrange(1,10)) #Here 10 is not included as range

#shuffel() used to shuffel the list of values
l=[10,20,30,40]
random.shuffle(l)
print(l)

#uniform()  it will generate the float values with in the range
print(random.uniform(10,20))

#sample()  it will generate sample form of data
list=["Rama","seetha","Geetha","Harini"]
print(random.sample(list,3))   #here 3 indicates return 3 items in list

print(random.sample(range(100),6))


#choice() it will give any one value as output from list
list=[10,20,30,40]
print(random.choice(list))

#String characters in random 
import random

s = "abcdef"
print(random.choice(s))  # Output could be 'a', 'b', ..., 'f'
