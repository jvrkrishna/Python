'''
__dict__ is an a varible in objects that stores their instance variable as a dictionary like key-value pair. It is useful for debugging or inspecting.
'''

#Example:
class Myclass:
    name="Ram" 
    def __init__(self):
        self.a=10  #instance variable
        self.b=20  #Instance variable

obj=Myclass()
print(obj.__dict__)