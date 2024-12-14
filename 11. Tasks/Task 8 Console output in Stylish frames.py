#Console output in stylish frame
'''To put the console output in stylish frame we have to go through "unicode box drawings"
By using the characters we can create fancy looking borders for the frames and tables.'''

#To draw the frame choose our border style(single, double, dash, border thichness.)
vertical='\u2551'
horizontal='\u2550'
top_left='\u2554'
top_right='\u2557'
bottom_left='\u255a'
bottom_right='\u255d'

Name=input('What is your name:')
print(f"\t{top_left}{horizontal*(len(Name)+4)}{top_right}")

print(f"\t{vertical}  {Name}  {vertical}")

print(f"\t{bottom_left}{horizontal*(len(Name)+4)}{bottom_right}")


#WAP to print the console output in multiple lines
from datetime import date, datetime
import os

frame_style = int(input("Choose a frame style (0 - Single Line, 1 - Double Line, 2 - Rounded Corner): "))

match frame_style:
	case 0:
		vertical = '\u2502'
		horizontal = '\u2500'
		top_left = '\u250c'
		top_right = '\u2510'
		bottom_left = '\u2514'
		bottom_right= '\u2518'		
	case 1:
		vertical = '\u2551'
		horizontal = '\u2550'
		top_left = '\u2554'
		top_right = '\u2557'
		bottom_left = '\u255a'
		bottom_right= '\u255d'
	case 2:
		vertical = '\u2502'
		horizontal = '\u2500'
		top_left = '\u256d'
		top_right = '\u256e'
		bottom_left = '\u2570'
		bottom_right= '\u256f'

date = datetime.now().strftime("%a %d/%m/%Y")

line_1 = "Hello everyone!"

name = input("What's your name: ")
line_2 = f"My name is {name}."

country = input("Where are you from: ")
line_3 = f"I'm from {country}."

job_title = input("Job title: ")
line_4 = f"I'm a {job_title}."

line_5 = "My favorite languages are:"

languages = input("Programming languages: ").split()
if len(languages) == 1:
	line_6 = languages[0]
if len(languages) == 2:
	line_6 = languages[0] + " and " + languages[1]
if len(languages) >= 3:
	line_6 = ', '.join(languages[:-1]) + ", and " + languages[-1]

line_7 = 'Good to see you all!'

max_len = max(len(line_2), len(line_3), len(line_4), len(line_5), len(line_6))

os.system('cls')
print()
print(f"\t{top_left}{horizontal*(max_len+4)}{top_right}")
print(f"\t{vertical}  {date:>{max_len}}  {vertical}")
print(f"\t{vertical}  {line_1:^{max_len}}  {vertical}")

for line in [line_2, line_3, line_4, line_5, line_6]:
	print(f"\t{vertical}  {line:<{max_len}}  {vertical}")	

print(f"\t{vertical}  {line_7:^{max_len}}  {vertical}")
print(f"\t{bottom_left}{horizontal*(max_len+4)}{bottom_right}")



