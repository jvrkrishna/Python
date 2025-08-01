'''In Python, the terms call by value and call by reference don't apply in the traditional sense like in C or C++. However, understanding them helps clarify how Python handles function arguments.

🔹 What is Call by Value?
    Call by Value means that a copy of the variable's value is passed to the function. Changes inside the function do not affect the original variable.

✅ In Python (with Immutable Types):
Immutable types (like int, str, float, tuple) behave like call by value.

Example:
    def change_value(x):
        x = x + 5
        print("Inside function:", x)

    a = 10
    change_value(a)
    print("Outside function:", a)

Output:
    Inside function: 15
    Outside function: 10

Why?
int is immutable.
x gets a copy of the reference to a, but x = x + 5 creates a new integer object.
So, a remains unchanged.

🔹 What is Call by Reference?
Call by Reference means that a reference (address) to the original variable is passed. Changes inside the function affect the original variable.

✅ In Python (with Mutable Types):
Mutable types (like list, dict, set) behave like call by reference.

Example:
    def modify_list(lst):
        lst.append(100)
        print("Inside function:", lst)

    my_list = [1, 2, 3]
    modify_list(my_list)
    print("Outside function:", my_list)

Output:
    Inside function: [1, 2, 3, 100]
    Outside function: [1, 2, 3, 100]

Why?
list is mutable.

The same object is modified, so the change reflects outside the function.

🔸 So What Does Python Actually Use?
Python uses "call by object reference" (or "call by sharing"):
The reference to the object is passed.
Whether the object can be changed depends on whether it’s mutable or immutable.

🔄 Summary Table:
Type	                    Behavior	      Affects original?	   Example
int, str, tuple	Immutable → like Call by Value	❌ No	Variable stays the same
list, dict, set	Mutable → like Call by Reference	✅ Yes	Variable is modified'''

