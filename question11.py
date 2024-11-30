"""
11. Exchange the first and last characters of a string.
"""
def exchange_first_last(string):
    return string[-1] + string[1:-1] + string[0] if len(string) > 1 else string

print(exchange_first_last("hello"))