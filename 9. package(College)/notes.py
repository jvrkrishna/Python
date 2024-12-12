#What is Package
'''
Package is nothing but folder or directory.
package is a container where we can store similar sub-packages and modules.
'''

# __init__.py
'''
If a folder contains __init__.py file then it will be considered a python package(It is optional after python 3.2 version).
This __init__.py can be empty.
'''

#Example structure follow college
'''
college
    staff
        __init__.py
        teaching.py   
        non_teaching.py
    students
        __init__.py
        arts.py
        sceince.py
    __init__.py
    info.py
'''

"""
College_program.py
"""

#We can operate the operations somewhere from College package to College_program.py 
