"""
Lesson 9: Simple Data Analysis

Objectives:
- Store numbers in lists
- Compute min, max, and average
- Organize weekly data and find the hottest day

Tasks:
1) Given a list of 10 numbers, print min, max, and average.
2) Ask the user for 5 test scores and print the average.
3) Daily Temperature Tracker for a week.
"""

# TODO 1: Stats from a list
numbers = [12, 5, 8, 20, 3, 15, 7, 10, 22, 9]
avg = sum(numbers) / len(numbers)
print(f"Numbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Average: {avg:.2f}")

# TODO 2: Test scores
scores = []
print("Enter 5 test scores:")
for _ in range(5):
    score = float(input("> "))
    scores.append(score)
print(f"Average score: {sum(scores) / len(scores):.2f}")

# TODO 3: Weekly temperatures
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = []
print("Enter the temperature for each day of the week:")
for d in days:
    t = float(input(f"{d}: "))
    temps.append(t)

avg_temp = sum(temps) / len(temps)
hottest_temp = max(temps)
hottest_day = days[temps.index(hottest_temp)]
print(f"Average temperature: {avg_temp:.1f}")
print(f"Hottest day: {hottest_day} at {hottest_temp:.1f}°F")
