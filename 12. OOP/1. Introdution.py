# Object-Oriented Programming (OOP)
## What is OOP?
'''
**Object-Oriented Programming (OOP)** is a programming paradigm used to write programs efficiently by using **Classes** and **Objects**.

* OOP is suitable for developing **large and complex applications**.
* It follows the **DRY (Don't Repeat Yourself)** principle.
* In OOP, we wrap **data** and **functions** into a single unit called a **Class**.
* Python's OOP features are inspired by languages like C++.
'''

# Real-Life Example
'''Think about a **Student**.
A student has:

**Data (Properties):**
* Name
* Roll Number
* Marks

**Actions (Functions):**
* Study()
* WriteExam()
* DisplayDetails()'''

'''In OOP:
* **Class** → Blueprint of a student.
* **Object** → Actual student created from that blueprint.
'''

# Class and Object Example
```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Rahul", 101)
s2 = Student("Priya", 102)

print(s1.name)
print(s2.name)
```

**Output**
```python
Rahul
Priya
```

# Why Do We Need OOP?
## Without OOP (Procedure-Oriented Programming)
```python
student1_name = "Rahul"
student1_roll = 101

student2_name = "Priya"
student2_roll = 102

student3_name = "Amit"
student3_roll = 103
```

#Imagine there are **100 students**:
```python
student100_name
student100_roll
student100_marks
student100_phone
```

### Problems:
❌ Too many variables.
❌ Difficult to remember variable names.
❌ Hard to add new information.
❌ Updating and searching become difficult.

## Updating Data Without OOP
```python
student1_roll = 201
```
To update Rahul's roll number, we must remember that Rahul is `student1`.
With 100 students, this becomes confusing.

## Searching Data Without OOP
```python
if student1_name == "Priya":
    print(student1_roll)
elif student2_name == "Priya":
    print(student2_roll)
elif student3_name == "Priya":
    print(student3_roll)
```

#As the number of students increases, the code becomes lengthy and difficult to maintain.

# With OOP
```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Rahul", 101)
s2 = Student("Priya", 102)
s3 = Student("Amit", 103)
```

Each object stores its own data:
```python
s1 → name="Rahul", roll=101
s2 → name="Priya", roll=102
s3 → name="Amit", roll=103
```

## Updating Data in OOP
```python
s1.roll = 201
print(s1.roll)
```

**Output**
```python
201
```

## Searching Data in OOP
```python
students = [
    Student("Rahul", 101),
    Student("Priya", 102),
    Student("Amit", 103)
]

for student in students:
    if student.name == "Priya":
        print(student.roll)
```

**Output**
```python
102
```

# Best Analogy for Students
### Without OOP
Student details are like **loose papers scattered on a table**.

### With OOP
Each student has a separate **file/folder** containing all their details.

Therefore, OOP makes data:
✅ Organized
✅ Easy to update
✅ Easy to search
✅ Easy to manage

# Advantages of OOP
### 1. Scalability
Large applications can grow easily.

### 2. Reusability
Write code once and use it many times.

### 3. Modularity
Programs are divided into small classes.

### 4. Flexibility
Easy to modify and extend.

### 5. Security
Data can be protected.

# Principles of OOP (Four Pillars)
## 1. Encapsulation 🔒
Wrapping data and functions into a single unit called a class.

```python
class Student:
    def __init__(self):
        self.name = "Rahul"
```

**Example:** A capsule contains medicine and its cover together.

## 2. Abstraction 🎭
Showing only important details and hiding implementation details.

```python
class Car:
    def start(self):
        print("Car Started")
```

You drive a car without knowing how the engine works.
---

## 3. Inheritance 👨‍👩‍👦
One class acquires properties and methods from another class.

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```

**Output**
```python
Animal makes sound
```

## 4. Polymorphism 🎨
One method behaves differently for different objects.
```python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.sound()
```

**Output**
```python
Bark
Meow
```
