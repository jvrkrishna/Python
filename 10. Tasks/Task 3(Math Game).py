from random import randint
import os
import time 

correct=0
wrong=0
level=int(input("Choose Difficulty Level(1= Easy, 2=Medium, 3=Hard):"))
Difficulty_level="None"
if level==1:
    Difficulty_level="Easy"
elif level==2:
    Difficulty_level="Medium"
elif level==3:
    Difficulty_level="Hard"
    
# store starting time 
begin = time.time() 

for i in range(10):
    os.system("cls") #To clear the screen
    a=randint(1,50)
    b=randint(1,50)
    c=a+b
    question=randint(1,3)
    print(f"Difficulty Level :{Difficulty_level}  |   Questions: {i}/10   |   Correct Answers: {correct}   |  Wrong Answers: {wrong}")
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
        print("Correct. Press Enter to continue...")
        correct=correct+1
        input() #pause the program wait for Enter.
    else:
        print("Not Correct.")
        wrong=wrong+1

time.sleep(1) 
# store end time 
end = time.time() 

if correct==10:
    grade="A"
elif correct in range(7,10):
    grade="B"
elif correct in range(5,7):
    grade="C"
else:
    grade="D"
    
      
print("Your Test Result:")
print(f"   >Scores: {correct}/10 ({correct/10*100} %)")
print(f"   >Time to complete: {end-begin} seconds")
print(f"   >Grade : {grade}")
        