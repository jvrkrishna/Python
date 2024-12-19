class Parrot():
# instance attributes
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
        
# instance method 
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object 
blu = Parrot("Blu", 10)
print(blu)

# call our instance methods 
print(blu.sing("'Happy'")) 
print(blu.dance())
