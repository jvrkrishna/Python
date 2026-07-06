# Passing One Class Object (or Members) to Another Class in Python
## Common Objects Used in All Programs
s1 = Student("Ram", 30)
s2 = Staff()
'''
* `s1` → object of `Student`
* `s2` → object of `Staff` (needed only for instance methods)'''

# 1. Instance Method + Complete Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Staff:
    def modify(self, x):
        x.age = 31

s1 = Student("Ram", 30)

print("Before:")
s1.details()

s2 = Staff()
s2.modify(s1)

print("After:")
s1.details()

### Output
'''Before:
Name : Ram
Age  : 30

After:
Name : Ram
Age  : 31

### Memory
x ───► Student Object ◄─── s1
          age = 31
**Original object changes because the complete object is passed.**
'''

# 2. Instance Method + One Member
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Staff:
    def modify(self, x):
        print("Received:", x)
        x = 31
        print("Changed x to:", x)

s1 = Student("Ram", 30)

print("Before:")
s1.details()

s2 = Staff()
s2.modify(s1.age)

print("After:")
s1.details()

### Output
'''Before:
Name : Ram
Age  : 30

Received: 30
Changed x to: 31

After:
Name : Ram
Age  : 30

### Memory
x = 30
s1.age = 30

**Original object does not change because only the value is passed.**'''

# 3. Class Method + Complete Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Staff:
    @classmethod
    def modify(cls, x):
        x.age = 31

s1 = Student("Ram", 30)

print("Before:")
s1.details()

Staff.modify(s1)

print("After:")
s1.details()

### Output
'''Before:
Name : Ram
Age  : 30

After:
Name : Ram
Age  : 31

### Memory
x ───► Student Object ◄─── s1
          age = 31

**Original object changes because the complete object is passed.**
'''

# 4. Class Method + One Member
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Staff:
    @classmethod
    def modify(cls, x):
        print("Received:", x)
        x = 31
        print("Changed x to:", x)

s1 = Student("Ram", 30)

print("Before:")
s1.details()

Staff.modify(s1.age)

print("After:")
s1.details()

### Output
'''Before:
Name : Ram
Age  : 30

Received: 30
Changed x to: 31

After:
Name : Ram
Age  : 30

### Memory
x = 30
s1.age = 30

**Original object does not change because only the value is passed.**'''

# 5. Static Method + Complete Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Staff:
    @staticmethod
    def modify(x):
        x.age = 31

s1 = Student("Ram", 30)

print("Before:")
s1.details()

Staff.modify(s1)

print("After:")
s1.details()

### Output
'''Before:
Name : Ram
Age  : 30

After:
Name : Ram
Age  : 31

### Memory
x ───► Student Object ◄─── s1
          age = 31

**Original object changes because the complete object is passed.**'''

# 6. Static Method + One Member
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Staff:
    @staticmethod
    def modify(x):
        print("Received:", x)
        x = 31
        print("Changed x to:", x)

s1 = Student("Ram", 30)

print("Before:")
s1.details()

Staff.modify(s1.age)

print("After:")
s1.details()

### Output
'''Before:
Name : Ram
Age  : 30

Received: 30
Changed x to: 31

After:
Name : Ram
Age  : 30

### Memory
x = 30
s1.age = 30

**Original object does not change because only the value is passed.**'''

# Final Comparison Table
'''
| Method Type     | Call                   | What is Passed? | `s1.age` Changes?|
| --------------- | ---------------------- | --------------- | ---------------- |
| Instance Method | `s2.modify(s1)`        | Complete object | ✅ Yes           |
| Instance Method | `s2.modify(s1.age)`    | Only value      | ❌ No            |
| Class Method    | `Staff.modify(s1)`     | Complete object | ✅ Yes           |
| Class Method    | `Staff.modify(s1.age)` | Only value      | ❌ No            |
| Static Method   | `Staff.modify(s1)`     | Complete object | ✅ Yes           |
| Static Method   | `Staff.modify(s1.age)` | Only value      | ❌ No            |'''

