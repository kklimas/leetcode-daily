nums1 = [1, 2, 3]
nums2 = [2, 4]


def get_common(array1, array2):
    i1, i2, n1, n2 = 0, 0, len(array1), len(array2)
    while i1 < n1 and i2 < n2:
        if array1[i1] < array2[i2]:
            i1 += 1
        elif array1[i1] > array2[i2]:
            i2 += 1
        else:
            return array1[i1]
    return -1


print(get_common(nums1, nums2))
