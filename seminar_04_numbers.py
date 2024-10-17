"""
Seminar 4 - Write the missing functions
Example Output:
Enter numbers separated by commas: 1,4.5,90, -2, 8,2
1.0..4.0..4.0..20.25..64.0..8100.0

"""
from string import ascii_uppercase


# print(ascii_uppercase)
# third_position = len(ascii_uppercase) // 3
# print(ascii_uppercase[:third_position])
# print(ascii_uppercase[third_position:third_position * 2 + 1])
# print(ascii_uppercase[-third_position - 1:])

def main():
    numbers = get_numbers()  # ABCDEFGH surname
    square_numbers(numbers)  # IJKLMNOPQ
    display_numbers(numbers)  # RSTUVWXYZ


def get_numbers():
    number_string = input("Enter numbers separate them by commas: ").split(',')
    numbers = [float(string) for string in number_string]
    return numbers


def square_numbers(numbers):
    """Square all the numbers in the list."""
    # numbers = [number ** 2 for number in numbers]
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2


def display_numbers(numbers):
    print("..".join(str(number) for number in sorted(numbers)))


main()
