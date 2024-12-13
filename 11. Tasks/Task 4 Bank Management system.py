'''Practical: WAP the activities of Bank to deposit and withdraw.'''
balance=1000
count=0
def Bank():
    password=int(input("Please enter the password to Login:"))
    key=2024
    if password==key:
        print("Congrats you successfully logged in...")
        
    else:
        if password!=key:
            print("Entered password is wrong...Please try again")
            global count
            count=count+1
            if(count==3):
                print("Sorry You have entered the worng password for three times please try after 24 hours")
                exit(0)
                Bank()
    print("Welcome to the Bank") 
    name=input("Enter the Name:")
    print("Hi",name,"Welcome to the Bank...")
    print("The current Balance is:",balance)
    ask() 
    
        
def ask():
    choice=int(input("How may Help You! *** For Deposit press 1 *** For Withdraw Press 2:"))
    if(choice==1):
        Deposit()
        extend()
        
    if(choice==2):
        Withdraw()
        extend()
       

def Deposit():
    amount=int(input("Enter the amount you want to Deposit! :"))
    global balance
    balance=balance+amount
    print("Congratulations your amount is deposited successfully!")
    print("The current balance is: ",balance)
        
def Withdraw():
    amount=int(input("Enter the amount you want to Withdraw! :"))
    global balance
    if(amount<balance):
        balance=balance-amount
        print("Congratulations your Withdraw processed successfully!..")
        print("The current balance is: ",balance)
        
def extend():
    option=input("Do you want to Continue or not if yes press y else press n: ")
    if(option=='y'):
        ask()
    else:
        exit(0)
         
        
Bank()
        
    
