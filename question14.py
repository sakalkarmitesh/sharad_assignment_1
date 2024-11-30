"""
14. Print unique words in sorted order from a comma-separated input.
"""
def sorted_unique_words():
    user_input = input("Enter comma-separated words: ")
    words = user_input.split(',')
    print(', '.join(sorted(set(words))))

# Uncomment to test
sorted_unique_words()