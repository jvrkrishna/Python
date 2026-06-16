# ------------------------------------
# 1. FOR LOOP
# Used when number of iterations is known
# ------------------------------------
for i in range(5):
    print(i)

# ------------------------------------
# 2. RANGE()
# range(start, stop, step)
# ------------------------------------
for i in range(1, 11, 2):
    print(i)

# ------------------------------------
# 3. PRINT IN SAME LINE
# ------------------------------------
for i in range(10):
    print(i, end=" ")

print()

# ------------------------------------
# 4. TAKE INPUT AND PRINT NUMBERS
# ------------------------------------
n = int(input("Enter limit: "))
for i in range(n):
    print(i)

# ------------------------------------
# 5. LOOP THROUGH STRING
# ------------------------------------
for ch in "Rama Krishna":
    print(ch)

# ------------------------------------
# 6. SKIP CHARACTERS IN STRING
# ------------------------------------
name = "Krishna"

for i in range(0, len(name), 2):
    print(name[i])

# ------------------------------------
# 7. LOOP THROUGH LIST
# ------------------------------------
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# ------------------------------------
# 8. MULTIPLICATION TABLE
# ------------------------------------
num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")

# ------------------------------------
# 9. WHILE LOOP
# Used when iterations are unknown
# ------------------------------------
i = 0

while i < 5:
    print(i)
    i += 1

# ------------------------------------
# 10. BREAK
# Stops loop immediately
# ------------------------------------
for i in range(10):
    if i == 5:
        break
    print(i)

# ------------------------------------
# 11. CONTINUE
# Skip current iteration
# ------------------------------------
for i in range(5):
    if i == 2:
        continue
    print(i)

# ------------------------------------
# 12. PASS
# Placeholder
# ------------------------------------
for i in range(3):
    pass

# ------------------------------------
# 13. REMOVE CHARACTER FROM STRING
# ------------------------------------
name = "Rama"
for i in name:
    if i == "a":
        continue
    print(i, end="")

# ------------------------------------
# 14. LOOP ELSE
# Executes after loop completes
# ------------------------------------
for i in range(3):
    print(i)
else:
    print("Loop completed")

# ------------------------------------
# 15. NESTED LOOP
# ------------------------------------
for i in range(3):
    for j in range(2):
        print(i, j)

# ------------------------------------
# 16. ENUMERATE
# Index + Value
# ------------------------------------
fruits = ["apple", "banana"]

for index, value in enumerate(fruits):
    print(index, value)

# ------------------------------------
# 17. ZIP
# Multiple lists together
# ------------------------------------
names = ["Ram", "Hari"]
marks = [90, 80]

for i, j in zip(names, marks):
    print(i, j)

# ------------------------------------
# 18. PRINT WITHOUT SPACES
# Example: Input=5 Output=12345
# ------------------------------------
n = int(input("Enter number: "))
for i in range(1, n+1):
    print(i, end="")

