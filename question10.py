"""
10. Remove the nth index character from a string.
"""
def remove_nth_char(string, n):
    return string[:n] + string[n+1:]

print(remove_nth_char("hello", 2))