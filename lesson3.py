"""
Lesson 3: Making Decisions in Code

Objectives:
- Use if/else statements
- Compare values using operators
- Practice boolean logic

Tasks:
1) Check if a number is positive, negative, or zero.
2) Password check.
3) Weather advisor.
"""

# TODO 1: Positive/negative/zero check
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# TODO 2: Password check
password = input("Enter password: ")
if password == "Python123":
    print("Access granted")
else:
    print("Access denied")

# TODO 3: Weather advisor
temp = float(input("Enter temperature (F): "))
if temp < 50:
    print("Wear a coat")
elif temp <= 65:
    print("A light jacket is fine")
else:
    print("Short sleeves today!")
