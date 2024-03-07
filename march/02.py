test_data = [([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]), ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])]


def solution(nums):
    n = len(nums)
    if n == 0:
        return nums
    if n == 1:
        nums[0] = nums[0] ** 2
        return nums

    result = [0 for _ in range(n)]
    l, r, res_i = 0, 1, 0

    while nums[r] < 0 and r < n - 1:
        l += 1
        r += 1
    while l > -1 or r < n:
        print(l, r, res_i)
        num_left = abs(nums[l]) if l > -1 else 10001
        num_right = abs(nums[r]) if r < n else 10001
        if num_left > num_right:
            result[res_i] = num_right ** 2
            r += 1
        else:
            result[res_i] = num_left ** 2
            l -= 1
        res_i += 1

    return result


print(solution([-10000, -9999, -7, -5, 0, 0, 10000]))
