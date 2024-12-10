#Date
import datetime as dt
d=dt.date(2024, 12, 10)   #year, month, day
print(d) 
print(d.year)
print(d.month)

#time
import datetime as dt
t=dt.time(10,30,15,7458)   #hours, min, sec, microsec
print(t)
print(t.minute)
print(t.microsecond)

#datetime
import datetime as dt
d_t=dt.datetime(2024, 12, 10, 10,30,15,7458)
print(d_t)

#Current Date and time
import datetime as dt
cdt=dt.datetime.now()
print(cdt)
print(cdt.hour)

#Wap to greet to user based on time
#6-12 morning, 12-18 afternoon, 18-22 good evening, 22-6 good night 
import datetime as dt
cdt=dt.datetime.now()
time=cdt.hour
if time>=6 and time<12:
    print("Hi Good morning")
elif time>=12 and time<6:
    print("Hi Good Afternoon")
elif time>=6 and time<22:
    print("Hi Good Evening")
else:
    print("Good Night")
    
#Day
import datetime as dt
cdt=dt.datetime.now()
print(cdt.strftime('%a'))   #for a ---mon
print(cdt.strftime('%A'))   #for A ---monday