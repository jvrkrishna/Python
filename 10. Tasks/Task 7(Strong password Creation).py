#Create 8 char password that must contain alphabets digits and special symbols.
import random
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits="0123456789"
special_symbols="~!@#$%^&*(_+=-{}[];/.><,:'"

print(random.choice(alpha),random.choice(digits),random.choice(special_symbols))

print(random.choice(alpha+digits+special_symbols),random.choice(digits+digits+special_symbols),random.choice(special_symbols+digits+special_symbols))

from random import randrange
for i in range(randrange(1,2)):
    print(random.choice(alpha+digits+special_symbols),random.choice(digits+digits+special_symbols),random.choice(special_symbols+digits+special_symbols),random.choice(special_symbols+digits+special_symbols))
    


    