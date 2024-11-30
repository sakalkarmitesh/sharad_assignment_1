"""
16. Convert a string to uppercase if it contains at least 2 uppercase characters in the first 4 characters.
"""
def to_upper_if_condition(string):
    if sum(1 for char in string[:4] if char.isupper()) >= 2:
        return string.upper()
    return string

print(to_upper_if_condition("HeLlo"))
print(to_upper_if_condition("hello"))
