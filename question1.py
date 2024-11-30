"""
1. Write a program that accepts a sentence and calculates the number of letters and digits.
"""
def count_letters_digits(sentence):
    letters = sum(char.isalpha() for char in sentence)
    digits = sum(char.isdigit() for char in sentence)
    print(f"LETTERS {letters}")
    print(f"DIGITS {digits}")

user_input = input("enter the string:")
count_letters_digits(user_input)