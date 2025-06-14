def sample(a):
    a=a+10 #Here we cannot append because int is immutable.
    print("Inside the function after Modification:",a)  #33
    print("Inside the function after Modification:",id(a))  #140706834617880

a=23  #Here int is immutable
sample(a)  #Calling Function
print("Outside the function after calling:",a)  #23
print("Outside the function after calling:",id(a))  #140706834615416