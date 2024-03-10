from collections import defaultdict


def intersection(nums1, nums2):
    result, d1, d2 = [], defaultdict(int), defaultdict(int)
    for n in nums1:
        d1[n] += 1
    for n in nums2:
        d2[n] += 1
    for key in d1:
        if d2[key] > 0:
            result.append(key)
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))