def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    # max robbed cash after visiting i-th house
    F = [0 for _ in range(n)]
    F[0] = nums[0]
    F[1] = nums[1]
    for i in range(2, n):
        x = max([F[j] for j in range(i - 1)])
        F[i] = max(F[i - 1], x + nums[i])

    return F[n - 1]


nums = [2, 7, 9, 3, 1]
print(rob(nums))
