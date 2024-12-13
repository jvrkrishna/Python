#Palindrome or not
'''A palindrome is a number or letter that remains the same even if the number and letters are reversed.'''

#Example:
string=input("Enter string: ") 
revstr="" 

for i in string:
    revstr=i+revstr 
print("Reversed string: ",revstr) 
 
if(string==revstr):
    print("The string is a palindrome.") 
else:
    print("The string is not a palindrome.")

#Example
def isPalindrome(string):
    if(string == string[::-1]): 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 
 
#Enter input string 
string = input("Enter string: ") 
 
print(isPalindrome(string))