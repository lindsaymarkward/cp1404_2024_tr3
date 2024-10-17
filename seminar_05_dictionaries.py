"""
CP1404 Seminar 5 - Internal TR3 2024
Produce the following sorted and formatted output
Bob         = 612
Xavier      =  80
Chantanelle =   9
Derek       =   7
"""
from operator import itemgetter

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]

max_length = max([len(name) for name, score in data])
for name, score in sorted(data, key=itemgetter(1), reverse=True):
    print(f"{name:{max_length}} = {score:3}", end="\n")
print("...")

# Now, what if this were a dictionary?
name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
for name, score in sorted(name_to_score.items(), key=itemgetter(1), reverse=True):
    print(f"{name:{max_length}} = {score:3}", end="\n")
print("...")

# Now using the get method as the key instead of sorting tuples of items
for name in sorted(name_to_score, key=name_to_score.get, reverse=True):
    print(f"{name:{max_length}} = {name_to_score[name]:3}", end="\n")

print(name_to_score)  # Notice the dictionary is unchanged, not sorted
print("...")

strings = ["a", "two", "lots and lots"]
# Long way of making a list
lengths = []
for string in strings:
    lengths.append(len(string))
print(lengths)

# Comprehension version - list
lengths = [len(string) for string in strings]  #
print(lengths)

# Long way of making a dict
string_to_length = {}
for string in strings:
    string_to_length[string] = len(string)
print(string_to_length)

# Comprehension version - dict
string_to_length = {string: len(string) for string in strings}
print(string_to_length)
