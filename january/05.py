"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence. test
"""


def longest_increasing_subsequence(numbers):
    n = len(numbers)
    length = 0
    T = [None for _ in range(n)]

    def binary_search(value, start, end):
        if start == end:
            return start
        if end - start == 1:
            if numbers[T[start]] >= value:
                return start
            return end

        middle = (start + end) // 2
        if numbers[T[middle]] > value:
            return binary_search(value, start, middle)
        return binary_search(value, middle, end)

    for i, number in enumerate(numbers):
        if T[length] is None:
            T[length] = i
        elif numbers[T[length]] < number:
            length += 1
            T[length] = i
        else:
            swap_index = binary_search(number, 0, length)
            T[swap_index] = i

    return length + 1


print(longest_increasing_subsequence([4, 10, 4, 3, 8, 9]))
