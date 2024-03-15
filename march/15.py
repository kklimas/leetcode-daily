import math


def product_expect_self(nums):
    # count 0's
    zeros = 0
    for num in nums:
        if num == 0:
            zeros += 1

    if zeros == 0:
        prod = math.prod(nums)
        for i in range(len(nums)):
            nums[i] = prod // nums[i]
        return nums
    if zeros == 1:
        prod_no_zero = math.prod([i for i in nums if i != 0])
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = prod_no_zero
            else:
                nums[i] = 0
        return nums
    return [0 for _ in range(len(nums))]
