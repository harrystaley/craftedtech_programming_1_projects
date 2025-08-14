"""
Lesson 10: Building a Simple Application – Guess the Number

Objectives:
- Combine input, loops, conditionals, and random numbers
- Give the user multiple attempts
- Provide feedback (too high / too low)

Task:
- Guess the Number game (1 to 20) with 5 attempts.
"""

import random

secret = random.randint(1, 20)
attempts = 5
print("I picked a number from 1 to 20. Can you guess it?")

for i in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {i}/{attempts} - Your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess == secret:
        print("Correct! You win!")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Sorry, you ran out of attempts. The number was {secret}.")
