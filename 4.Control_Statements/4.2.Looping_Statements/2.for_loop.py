for num in range(10):
    print(num)


for i in range(1,11,2):   #range(start,stop,skip)
    print(i)


for i in range(0,10):
    print(i,end = ' ')


n=int(input("Enter the number up to which you want to print the natural numbers:"))
for i in range(n):
    print(i)

#WAP to print the characters from a string
for i in "Rama Krishna":
    print(i)

#WAP to print the skipping characters from a string
a="Krishna"
n=len(a)
for i in range(0,n,2):
    print(a[i])
    

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


num = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

# No of iterations is known then we can use for loop   
n=0
for i in range(10):
    print(i)

# No of iteration is not known then we can use while
i=0   
while True:
    print(i)
    i=i+1
    
#WAP to print string by skipping some element       
def hide_char():
    name="Rama"
    char='a'
    count=0
    hidden_string=""
    for c in name:
        if c==char:
            hidden_string +=""
            
        else:
            hidden_string += c
    print(hidden_string)

hide_char()

#WAP to print string by skipping some element by using continue      
def hide_char():
    name="Rama"
    for i in name:
        if i=="a":
            continue
        print(i,end="")
hide_char()
    
# SAMPLE PROGRAM
# QUESTION:
'''The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between.'''

#Example
'''
Print the string .

Input Format
The first line contains an integer .
Constraints

Output Format
Print the list of integers from  through  as a string, without spaces.

Sample Input 0
3

Sample Output 0
123
'''

# Output:
if __name__ == '__main__':
    n = int(input())
    x=range(1,n+1)
    for i in x:
        print(i,end="")