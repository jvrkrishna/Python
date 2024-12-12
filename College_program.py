import College.info
#Accessing info module method
College.info.get_info()

#Accessing info module variable
print(College.info.estd)

#import non-teaching staff module
import College.staff.non_teaching
College.staff.non_teaching.non_teaching_staff()

#we can import like this as well
from College.staff import teaching
teaching.teaching_staff()

#We need not to call __init__.py file it will called automatically when we import package
import College