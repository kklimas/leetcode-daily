from collections import defaultdict


def find_error_num(nums):
    n = len(nums)
    d = defaultdict(int)
    for k in nums:
        d[k] += 1
    n1, n2 = -1, -1
    for k in range(1, n + 1):
        if d[k] == 2:
            n1 = k
        if d[k] == 0:
            n2 = k
    return [n1, n2]


nums = [1, 1]
print(find_error_num(nums))
