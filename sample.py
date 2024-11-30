def sample(a):   #Called function
    print("Inside the function before Modification:",a)  #[10, 20, 30]
    print("Inside the function before Modification:",id(a))  #2063865878784
    a.append(100)
    print("Inside the function before Modification:",a)  #[10, 20, 30, 100]
    print("Inside the function before Modification:",id(a))  #2063865878784

a=[10,20,30]  #Here list is mutable
print("Outside the function before calling:",a)  #[10, 20, 30]
print("Outside the function before calling:",id(a))  #2063865878784
sample(a)  #Calling Function
print("Outside the function after calling:",a)  #[10, 20, 30, 100]
print("Outside the function after calling:",id(a))  #2063865878784