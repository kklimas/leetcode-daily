def numSubarraysWithSum(nums, goal):
    return atMost(nums, goal) - atMost(nums, goal - 1)


def atMost(nums, goal):
    head, tail, total, result = 0, 0, 0, 0
    for head in range(len(nums)):
        total += nums[head]
        while total > goal and tail <= head:
            total -= nums[tail]
            tail += 1
        result += head - tail + 1
    return result
