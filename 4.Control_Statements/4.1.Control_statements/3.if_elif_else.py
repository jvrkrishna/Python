if(5<2):
    print("this is if")
elif(5<2):
    print("this is elif")
else:
    print("this is else")


#write a program to to check the student grade.
marks = int(input("Enter the marks: "))
if marks > 85 and marks <= 100:
    print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
    print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
    print("You scored grade B ...")
elif (marks > 30 and marks <= 40):
    print("You scored grade C ...")
else:
    print("Sorry you are fail ?")
