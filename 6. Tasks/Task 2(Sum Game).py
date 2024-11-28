#sum game with random numbers
from random import randint
count=0
while True:
    a=randint(1,50)
    b=randint(1,50)
    c=a+b
    question=randint(1,3)
    print("Type your answer: ")

    match question:
        case 1:
            print(f"? + {b}= {c}")
            correct_answer=a
        
        case 2:
            print(f"{a} + ?= {c}")
            correct_answer=b
        
        case 3:
            print(f"{a} + {b}= ?")
            correct_answer=c
    
    while True:
        try:
            your_answer=int(input())
            break
        except:
            print("Please Enter the numbers only")
        
    if your_answer==correct_answer:
        print("Correct. Please Enter to continue...")
        count=count+1
        input() #pause the program wait for Enter.
    else:
        print("Not Correct.")
        break

print(f"You have answered {count} questions Correctly")