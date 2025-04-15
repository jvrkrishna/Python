s1="welcome to python"
print(s1.startswith("welcome"))
print(s1.startswith("Welcome"))
print(s1.endswith("python"))
print(s1.endswith("Python"))

print(s1.isalpha())
s2="Welcometopython"  #Without spaces then it is alpha
print(s2.isalpha())

s2="1Welcometopython"
print(s2.isalnum())