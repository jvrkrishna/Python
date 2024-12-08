import random
guess=random.randint(1,10)
count=0

while True:
    count=count+1
    choice=(int(input("Guess the Number between 1 - 10: ")))
    
    if choice==guess:
        print("Congrats Your guess is correct.")
        break
    
    elif choice>guess:
        print("Oh your guess is greater than system generated number.")
        
    else:
        print("Oh your guess number is less than system generated number.")

print(f"You have taken {count} steps to guess the number.")