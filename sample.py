def sample(a):   #Called function
    print("Inside the function before Modification:",a)  #23
    print("Inside the function before Modification:",id(a))  #140706834615416
    a=100
    print("Inside the function before Modification:",a)  #100
    print("Inside the function before Modification:",id(a))  #140706834617880

a=23
print("Outside the function before calling:",a)  #23
print("Outside the function before calling:",id(a))  #140706834615416
sample(a)  #Calling Function
print("Outside the function after calling:",a)  #23
print("Outside the function after calling:",id(a))  #140706834615416