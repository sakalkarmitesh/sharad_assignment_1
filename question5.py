"""
5. Write a Python program to count the number of characters (character frequency) in a string.
"""
from collections import Counter

def char_frequency(string):
    return dict(Counter(string))

print(char_frequency("hello world"))