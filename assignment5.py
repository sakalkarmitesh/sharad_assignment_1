"""Problem Statement

Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run. Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input 1:
AAAABBBBCCCCCCCC
Expected Output 21:
4A4B8C
Sample Input 2:
AABCCA
Expected Output 2:
2A1B2C1A
"""

def encode(message):
    encoded_message = ""
    count = 1

    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            encoded_message += str(count) + message[i - 1]
            count = 1

    encoded_message += str(count) + message[-1]

    return encoded_message

message = "AAAABBBBCCCCCCCC"
encoded_message = encode(message)
print(encoded_message)