class Bank:
    bankname="Rk Bank"
    branch="XYZ, India"
    
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f"Hello {self.username} cong! your account created successfully")
        
    #deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} deposited successfully")
        
    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f"{amount} withdraw successfully")
        else:
            print('Insufficent Fund....')
            
    #checkbalance
    def checkbalance(self):
        print(f"Your account balance is {self.balance}")
        
print(f"Welcome to {Bank.bankname}, {Bank.branch}")        
username=input("Enter your Name:")
pan=input("Enter Pan Card Number:")
address=input("Enter your address:")

b=Bank(username,pan,address)    

while True:
    print('Please select any option :')
    print('1.Deposit \n2.Withdraw \n3.Check balance \n4.stop')
    option=int(input(''))
    
    if option==1:
        amount=float(input("Enter Deposited amount :"))
        b.deposit(amount)
        
    if option==2:
        amount=int(input("Enter withdraw amount :"))
        b.withdraw(amount)
        
    if option==3:
        b.checkbalance()
        
    if option==4:
        print("Thanks for using Indian Express Bank .....")
        break
    else:
        print("Please select valid option")