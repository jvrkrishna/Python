###Call By Value vs Call By reference

############ CALL BY VALUE ##################
'''If we made any chages on called function it will not reflect on outside the function when we call with value.'''

def sample(a):   #Called function
    print("Inside the function before Modification:",a)  #23
    print("Inside the function before Modification:",id(a))  #140706834615416
    a=100 #Here we cannot append because int is immutable.
    print("Inside the function after Modification:",a)  #100
    print("Inside the function after Modification:",id(a))  #140706834617880

a=23  #Here int is immutable
print("Outside the function before calling:",a)  #23
print("Outside the function before calling:",id(a))  #140706834615416
sample(a)  #Calling Function
print("Outside the function after calling:",a)  #23
print("Outside the function after calling:",id(a))  #140706834615416

############ CALL BY REFERENCE ##################
'''If we made any chages on called function it will reflect on outside the function when we call with reference.'''
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

###NOTE:
'''Python does not support Call by value or Call by reference it support by call by object reference. When we pass immutable objects like int,float, tuple it acts like call by value (i.e., modify that object and create new object.) and when we pass mutable objects like list, dictionary it acts like call by reference (i.e., modify that object and will not create new object.).'''
