"""
12. Remove characters with odd index values from a string.
"""
def remove_odd_index_chars(string):
    return string[::2]

print(remove_odd_index_chars("hello world"))