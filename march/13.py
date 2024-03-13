def pivot_integer(n: int) -> int:
    if n == 1:
        return 1
    bottom_sum = 1
    top_sum = sum([i for i in range(1, n + 1)])

    for i in range(2, n + 1):
        if bottom_sum == top_sum:
            return i - 1
        bottom_sum += i
        top_sum -= i - 1

    return -1