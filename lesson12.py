"""
Lesson 12: Project Work II – Build and Reflect

Objectives:
- Finish your personal project
- Write a short reflection about what you built and learned
- Save a summary to 'project_reflection.txt'

Instructions:
- Make sure your project code runs from a main Python file (e.g., my_project.py).
- Then run this script to record your reflection.
"""

print("Project Reflection")
title = input("Project title: ")
summary = input("Briefly describe what your program does: ")
learnings = input("What did you learn while building it? ")
challenges = input("What challenges did you face and how did you solve them? ")

with open("project_reflection.txt", "w", encoding="utf-8") as f:
    f.write("Project Title:\n" + title + "\n\n")
    f.write("Summary:\n" + summary + "\n\n")
    f.write("Learnings:\n" + learnings + "\n\n")
    f.write("Challenges and Solutions:\n" + challenges + "\n")

print("Saved project_reflection.txt")
