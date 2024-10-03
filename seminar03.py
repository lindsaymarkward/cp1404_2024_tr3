"""
Seminar 3 in-class demos.
Write a program to read a file and print ONLY the lines that start with a #
The user should enter the filename.
"""
DEFAULT_IN_FILENAME = "seminar01.py"

in_filename = input("Input Filename: ")
# in_filename = "seminar01.py"
# out_filename = "output.txt"
try:
    in_file = open(in_filename, 'r')
except FileNotFoundError:
    print(f"{in_filename} not found, using {DEFAULT_IN_FILENAME}")
    in_filename = DEFAULT_IN_FILENAME
    in_file = open(in_filename, 'r')
out_filename = input("Output Filename: ")
out_file = open(out_filename, 'w')
for line in in_file:
    if line.startswith('#'):
        print(line.strip(), file=out_file)
in_file.close()
out_file.close()

# strings = ['Bob', 'fish', 'abc123']
