"""
6. Write a Python program to get a string made of the first 2 and the last 2 chars of a given string.
"""
def first_last_chars(string):
    return string[:2] + string[-2:] if len(string) >= 2 else ""

print(first_last_chars("hello"))
print(first_last_chars("hi"))
print(first_last_chars("a"))