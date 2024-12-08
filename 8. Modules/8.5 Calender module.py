import calendar as c
print(list(c.day_name))

for i in c.day_name:
    print(i)
    
for i in c.day_name:
    print(i[:-3])
    
#print abbrevations of day_name 
for i in c.day_abbr:
    print(i)
    
help(c.day_abbr) #if you want to know about abbr

print(list(c.month_name))

#Leap year or not
print(c.isleap(2024))

print(c.leapdays(2000,2024))

print(c.weekheader(1))

print(c.calendar(2024))

print(c.monthcalendar(2024,12))