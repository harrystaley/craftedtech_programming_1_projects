"""
Lesson 7: Working with Text Files

Objectives:
- Write text to a file
- Read text from a file
- Append new content without overwriting old content

Tasks:
1) Create a file notes.txt and write three lines.
2) Open notes.txt and print each line.
3) Simple Journal: prompt for an entry, append to journal.txt, then show all entries.
"""

# TODO 1: Write to notes.txt
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("First note\n")
    f.write("Second note\n")
    f.write("Third note\n")
print("Wrote notes.txt")

# TODO 2: Read notes.txt
print("Reading notes.txt:")
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# TODO 3: Simple Journal
entry = input("Journal entry: ")
with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(entry + "\n")

print("All journal entries so far:")
with open("journal.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
