"""
2. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
"""
def add_ing(string):
    if len(string) >= 3:
        if string.endswith('ing'):
            return string + 'ly'
        return string + 'ing'
    return string

user_input = input("enter input string")
print(add_ing(user_input))