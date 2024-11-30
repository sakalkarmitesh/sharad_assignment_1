"""
18. Remove a newline character from a string.
"""
def remove_newline(string):
    return string.replace('\n', '')

print(remove_newline("hello\nworld"))