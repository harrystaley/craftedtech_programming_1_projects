"""
Lesson 5: Collections – Lists and Dictionaries

Objectives:
- Create and use lists and dictionaries
- Access items by index and key
- Iterate over collections

Tasks:
1) Make a list of 5 favorite foods and print each one with a loop.
2) Create a country->capital dictionary and look up a capital from user input.
3) Grocery List Manager: add 3 items entered by the user, then print the list.
"""

# TODO 1: Favorite foods list
foods = ["pizza", "sushi", "tacos", "pasta", "salad"]
for food in foods:
    print(f"I like {food}")

# TODO 2: Capitals dictionary
capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
}
country = input("Enter a country (USA, France, Japan): ")
if country in capitals:
    print(f"The capital of {country} is {capitals[country]}")
else:
    print("I don't know that country yet.")

# TODO 3: Grocery List Manager
grocery_list = []
print("Add 3 grocery items:")
for _ in range(3):
    item = input("Item: ")
    grocery_list.append(item)
print("Your grocery list:")
for idx, item in enumerate(grocery_list, start=1):
    print(f"{idx}. {item}")
