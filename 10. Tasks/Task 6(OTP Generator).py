#Generate otp in manual process
import random
print(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

#Generate otp using loop
import random
otp=""
for i in range(6):
    otp=otp+str(random.randint(0,9))
print(otp)

#Example
import random
print(random.randint(1000,9999)) #One drawback is there otp is every time greater that 1000

