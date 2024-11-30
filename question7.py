"""
7. Write a Python program to replace all occurrences of the first char of a string with '$', except the first char itself.
"""
def replace_with_dollar(string):
    return string[0] + string[1:].replace(string[0], '$') if string else ""

print(replace_with_dollar("restart"))