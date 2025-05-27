#Access Modifiers ---- public, protected, private
class college:
    def __init__(self):
        self.__x=100
    def sample(self):
        print(self.__x)
class college1(college):
    def sample1(self):
        print(self.__x)
c=college()
c.sample()

# c1=college1()
# c1.sample1()

print(c._college__x)