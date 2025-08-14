"""
Lesson 11: Project Work I – Planning and Pseudocode

Objectives:
- Choose a simple project idea (1–2 sentences)
- Identify which concepts you'll use
- Write pseudocode (steps) before coding

This script will guide you to create a 'project_plan.txt' file.
"""

print("Let's plan your project.")
idea = input("Describe your project in 1–2 sentences: ")
concepts = input("Which Python concepts will you need? (e.g., variables, loops, functions, files): ")

print("Now, write your pseudocode (type steps; blank line to finish):")
steps = []
while True:
    line = input("> ")
    if line.strip() == "":
        break
    steps.append(line)

with open("project_plan.txt", "w", encoding="utf-8") as f:
    f.write("Project Idea:\n")
    f.write(idea + "\n\n")
    f.write("Concepts Needed:\n")
    f.write(concepts + "\n\n")
    f.write("Pseudocode Steps:\n")
    for s in steps:
        f.write("- " + s + "\n")

print("Saved project_plan.txt")
