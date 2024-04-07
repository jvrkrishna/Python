x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

