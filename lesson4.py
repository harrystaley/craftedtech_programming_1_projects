"""
Lesson 4: Repeating Tasks with Loops

Objectives:
- Practice for loops and while loops
- Use range() to generate sequences
- Build a simple multiplication table

Tasks:
1) Print the numbers 1 to 10 using a for loop.
2) Ask for numbers until the user enters 0 (while loop).
3) Multiplication Table Generator for a number from 1 to 10.
"""

# TODO 1: for loop 1..10
for i in range(1, 11):
    print(i)

# TODO 2: while loop until 0
print("Enter numbers (0 to stop):")
while True:
    value = float(input("> "))
    if value == 0:
        print("Stopping.")
        break
    print(f"You entered: {value}")

# TODO 3: Multiplication table
n = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
