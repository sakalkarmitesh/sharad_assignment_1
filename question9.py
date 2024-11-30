"""
9. Replace the 'not'...'poor' substring with 'good'.
"""
def replace_not_poor(string):
    not_idx = string.find('not')
    poor_idx = string.find('poor')
    if not_idx != -1 and poor_idx != -1 and not_idx < poor_idx:
        return string[:not_idx] + 'good' + string[poor_idx + 4:]
    return string

print(replace_not_poor("The movie is not that poor"))