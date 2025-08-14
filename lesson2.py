"""
Lesson 2: Basic Data Types

Objectives:
- Work with numbers and strings
- Store values in variables
- Perform simple math operations

Tasks:
1) Store your age in a variable and print it.
2) Ask the user for two numbers and print their sum, difference, product, and quotient.
3) Create a trip cost estimator.
"""

# TODO 1: Store your age in a variable and print it
age = 35  # You can change this
print(f"My age is {age}")

# TODO 2: Ask for two numbers and print operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
if num2 != 0:
    print(f"Quotient: {num1 / num2}")
else:
    print("Cannot divide by zero.")

# TODO 3: Trip cost estimator
miles = float(input("Enter miles to travel: "))
mpg = float(input("Enter miles per gallon: "))
cost_per_gallon = float(input("Enter cost per gallon: "))
total_cost = (miles / mpg) * cost_per_gallon
print(f"Estimated fuel cost: ${total_cost:.2f}")
