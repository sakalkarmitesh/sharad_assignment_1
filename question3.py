"""
3. Write a Python function that takes a list of words and returns the length of the longest one.
"""
def longest_word(words):
    return max(len(word) for word in words)

print(longest_word(['apple', 'banana', 'cherry']))