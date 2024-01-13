"""
You are given two strings of the same length s and t. In one step you can choose any character of t and
 replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""


def min_steps(s, t):
    result_dict = dict()
    operations = 0
    for letter in s:
        if letter in result_dict:
            result_dict[letter] = result_dict[letter] + 1
            continue
        result_dict[letter] = 1
    for letter in t:
        if letter in result_dict:
            if result_dict[letter] > 0:
                result_dict[letter] = result_dict[letter] - 1
            else:
                operations += 1
            continue
        operations += 1

    return operations


s = 'anagram'
t = 'mangaar'
print(min_steps(s, t))
