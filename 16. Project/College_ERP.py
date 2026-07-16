students = []
count = 0

USERNAME = "admin"
PASSWORD = 2024

def CollegeERP():
    global count

    while count < 3:
        username = input("Enter Username : ")
        password = int(input("Enter Password : "))

        if username == USERNAME and password == PASSWORD:
            print("\nLogin Successful...")
            break
        else:
            count += 1
            print("Invalid Username or Password\n")

    if count == 3:
        print("You entered wrong credentials 3 times.")
        exit()

    print("\n***** WELCOME TO COLLEGE ERP *****")
    admin = input("Enter Admin Name : ")
    print(f"Welcome {admin}\n")

    Menu()


def Menu():

    while True:

        print("\n===== COLLEGE ERP MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            AddStudent()

        elif choice == 2:
            ViewStudents()

        elif choice == 3:
            SearchStudent()

        elif choice == 4:
            UpdateStudent()

        elif choice == 5:
            DeleteStudent()

        elif choice == 6:
            print("Thank You...")
            exit()

        else:
            print("Invalid Choice")


def AddStudent():

    student = {}

    student["id"] = input("Enter Student ID : ")
    student["name"] = input("Enter Student Name : ")
    student["branch"] = input("Enter Branch : ")
    student["year"] = input("Enter Year : ")
    student["section"] = input("Enter Section : ")

    students.append(student)

    print("Student Added Successfully...")


def ViewStudents():

    if len(students) == 0:
        print("No Student Records Found")
        return

    print("\n------ STUDENT LIST ------")

    for student in students:

        print("------------------------")
        print("ID :", student["id"])
        print("Name :", student["name"])
        print("Branch :", student["branch"])
        print("Year :", student["year"])
        print("Section :", student["section"])


def SearchStudent():

    sid = input("Enter Student ID : ")

    for student in students:

        if student["id"] == sid:

            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found")


def UpdateStudent():

    sid = input("Enter Student ID : ")

    for student in students:

        if student["id"] == sid:

            student["name"] = input("Enter New Name : ")
            student["branch"] = input("Enter New Branch : ")
            student["year"] = input("Enter New Year : ")
            student["section"] = input("Enter New Section : ")

            print("Student Updated Successfully")
            return

    print("Student Not Found")


def DeleteStudent():

    sid = input("Enter Student ID : ")

    for student in students:

        if student["id"] == sid:

            students.remove(student)

            print("Student Deleted Successfully")
            return

    print("Student Not Found")


CollegeERP()