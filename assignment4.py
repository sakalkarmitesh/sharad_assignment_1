"""Problem Statement

Write a python function, create _largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. Note: Assume that all the numbers are two digit numbers.

Sample Input:
23,34,55
Expected Output:
553423
"""

def create_largest_number(number_list):
    # Sort the list in descending order based on a custom comparison function
    number_list.sort(key=lambda x: x * 10 + (x // 10), reverse=True)

    # Concatenate the sorted numbers
    largest_number = ''.join(str(num) for num in number_list)
    return int(largest_number)

number_list = [23, 34, 55]
largest_number = create_largest_number(number_list)
print(largest_number)  # Output: 553423