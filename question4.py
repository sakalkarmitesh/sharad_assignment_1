"""
4. Write a Python program to check if a string contains all letters of the alphabet.
"""
def contains_all_alphabet(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(string.lower())

print(contains_all_alphabet("The quick brown fox jumps over the lazy dog"))
print(contains_all_alphabet("Hello World"))
