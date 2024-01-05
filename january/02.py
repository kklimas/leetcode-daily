"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

    The 2D array should contain only the elements of the array nums.
    Each row in the 2D array contains distinct integers.
    The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""

numbers = [1,2,3,4]


def find_matrix(numbers):
    n = len(numbers)
    if n == 0:
        return []
    if n == 1:
        return [[numbers[0]]]

    numbers_dict = {}
    rows = 1
    for number in numbers:
        if number in numbers_dict:
            value = numbers_dict[number]
            numbers_dict[number] = value + 1
            rows = max(rows, value + 1)
        else:
            numbers_dict[number] = 1

    result = [[] for _ in range(rows)]
    for number in numbers:
        if number in numbers_dict:
            value = numbers_dict[number]
            print(number, value)
            if value - 1 >= 0:
                result[value - 1].append(number)
                numbers_dict[number] = value - 1
            else:
                numbers_dict.pop(number)

    print(result)


find_matrix(numbers)
