################ MANUAL Process without faker module ##################
#Create 3 to 13 char name that must contain only alphabets. 
from random import *
alpha="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

fname=''
for i in range(randint(3,13)):  #password in the range of 3 to 13 chars
    fname=fname+choice(alpha)
    
print(fname)

#WAP to print the names in different patterns
from random import *
alpha="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

for i in range(200):
    fname=''
    for i in range(randint(5,12)):  #names in the range of 3 to 13 chars
        fname=fname+choice(alpha)
    
    print(fname)
    

#WAP to print the names in different patterns of 50 names
from random import *
alpha="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

for i in range(50):
    fname=''
    for i in range(randint(5,12)):  #password in the range of 3 to 13 chars
        fname=fname+choice(alpha)
    
    print(fname)
    
#WAP to print the mobile 
from random import *
numbers="9876543210"
initial="+91 "
mno=initial+choice("9876")
for i in range(9):
    mno=mno+choice(numbers)

print(mno)

#WAP to print the no of  mobile 
from random import *
numbers="9876543210"
for i in range(10):
    initial="+91 "
    mno=initial+choice("9876")
    for i in range(9):
        mno=mno+choice(numbers)

    print(mno)
    
    
#WAP to print different addresses
from random import *
cities=["kkd","Samalkot","Pdp","Rjy","Vizag"]
address=choice(cities)
print(address)

#WAP to print different addresses with in range
from random import *
cities=["kkd","Samalkot","Pdp","Rjy","Vizag","Eluru","Razole"]
for i in range(20):
    address=choice(cities)
    print(address)
    
############# Automation with faker Modules ############
from faker import Faker    
fk=Faker()

print("Name:",fk.name())
print("Email:",fk.email())
print("Address:",fk.address())
print("Country: ", fk.country())
print("Website:", fk.url())
print("Message:",fk.text())
print("Name:",fk.file_name(), fk.last_name())
print("Time:",fk.time(), fk.am_pm())
print("Mobile No:",fk.phone_number())

print("My profile is:",fk.profile())

#Faker.seed(1)  #This is used to freeze one output without changing this faker.seed(1) is use before from which line we want to freeze 

fk=Faker('hi-IN')
print(fk.name())