"""
Problem Statement
Write a python program which displays the count of the names that matches a given pattern from a list of names provided.
Consider the pattern characters to be:
1. "at" where "" can be one occurrence of any character
2. "%at%" where "%" can have zero or any number of occurrences of a character

Sample Input:
[Hat, Cat, Rabbit, Matter]
Expected Output:
at -> 2 %at% -> 3"""

def count_names(name_list):
    count1 = 0
    count2 = 0

    for name in name_list:
        if name.endswith("at"):
            count1 += 1
        if "at" in name:
            count2 += 1

    print("at -> ", count1)
    print("%at% -> ", count2)

name_list = ["Hat", "Cat", "Rabbit", "Matter"]
count_names(name_list)