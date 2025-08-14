"""
Lesson 8: Introduction to Error Handling

Objectives:
- Use try/except to catch exceptions
- Handle invalid user input
- Prevent crashes (e.g., division by zero)

Tasks:
1) Ask for a number and print its square. Handle non-number input.
2) Try to open a file; print 'File not found' if missing.
3) Safe Calculator: divide two numbers with error handling.
"""

# TODO 1: Square a number with error handling
value = input("Enter a number to square: ")
try:
    num = float(value)
    print(f"Square: {num * num}")
except ValueError:
    print("That was not a number.")

# TODO 2: Try opening a file
filename = input("Enter a filename to open: ")
try:
    with open(filename, "r", encoding="utf-8") as f:
        print("File contents:")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")

# TODO 3: Safe Calculator (division)
try:
    a = float(input("Enter dividend: "))
    b = float(input("Enter divisor: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
