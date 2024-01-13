"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the
 first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
 Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


def halves_are_like(s):
    n = len(s)
    half = n // 2
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter = 0

    for i, letter in enumerate(s):
        sign = 1
        if i >= half:
            sign = -1
        if letter in vowels:
            counter += sign
    return counter == 0


print(halves_are_like('AbCdEfGh'))