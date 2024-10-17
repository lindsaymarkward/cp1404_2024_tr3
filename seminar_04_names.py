"""
Seminar 4 - Lists
Given a list of names, prompt the user to remove names
until they enter an empty string.
Ensure the program does not crash when the name is not in the list.
"""

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        pass
    print(", ".join(names))
    name_to_remove = input("Who do you want to remove? ")
print(", ".join(names))
