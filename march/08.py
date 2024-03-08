from collections import defaultdict


def max_frequency_elements(nums):
    dc = defaultdict(int)
    for num in nums:
        dc[num] += 1
    max_val = max(dc.values())
    return sum([k for k in dc.values() if k == max_val])


nums = [1, 2, 2, 3, 1, 4]
print(max_frequency_elements(nums))
