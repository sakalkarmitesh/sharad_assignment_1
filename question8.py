"""
8. Write a Python program to swap the first two characters of each of two given strings and join them with a space.
"""
def swap_and_combine(str1, str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

print(swap_and_combine("hello", "world"))
