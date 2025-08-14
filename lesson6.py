"""
Lesson 6: Writing Reusable Code with Functions

Objectives:
- Define and call functions with parameters
- Return values from functions
- Test functions with user input

Tasks:
1) Write a function greet(name) that prints a greeting.
2) Write a function average(a, b) that returns the average of two numbers.
3) Tip Calculator Function: total_with_tip(cost, tip_percent) -> total.
"""

# TODO 1: greet function
def greet(name):
    print(f"Hello, {name}!")

user_name = input("Enter your name: ")
greet(user_name)

# TODO 2: average function
def average(a, b):
    return (a + b) / 2

x = float(input("Enter first number for average: "))
y = float(input("Enter second number for average: "))
print(f"Average: {average(x, y)}")

# TODO 3: tip calculator function
def total_with_tip(cost, tip_percent):
    tip = cost * (tip_percent / 100.0)
    return cost + tip

meal = float(input("Enter meal cost: "))
tip_pct = float(input("Enter tip percent (e.g., 18): "))
print(f"Total with tip: ${total_with_tip(meal, tip_pct):.2f}")
