"""
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

    Choose two elements with equal values and delete them from the array.
    Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
"""

def min_operations(numbers):
    num_dict = {}
    result = 0
    for number in numbers:
        if number in num_dict:
            num_dict[number] = num_dict[number] + 1
        else:
            num_dict[number] = 1
    for value in num_dict.values():
        temp_result = better_search(value)
        if temp_result == -1:
            return -1
        result += temp_result
    return result


def better_search(number):
    tmp_number = number
    while tmp_number % 3 != 0 and tmp_number > 0:
        tmp_number -= 2

    # found number divided by three
    if tmp_number % 3 == 0:
        return tmp_number // 3 + (number - tmp_number) // 2

    if tmp_number == 0:
        return number // 2

    return -1


print(min_operations([152,152,152,152,152,152,152,152,152,152,152,152,215,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,114,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,152,215,152,152,152,152,152,152,152,152,114,152,152,152,152,152,114,152,152,152,114,152,152,152,114,152,152,152,114,152,152,152,152,152,215]))
