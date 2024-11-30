"""
15. Create a string of 4 copies of the last two characters of a given string.
"""
def repeat_last_two(string):
    return string[-2:] * 4 if len(string) >= 2 else ""

print(repeat_last_two("hello"))
print(repeat_last_two("hi"))
print(repeat_last_two("a"))