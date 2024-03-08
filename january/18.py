def climb_stairs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    saved_results = [0 for _ in range(n)]
    saved_results[0] = 1
    saved_results[1] = 2
    for i in range(2, n):
        saved_results[i] = saved_results[i - 1] + saved_results[i - 2]

    return saved_results[n - 1]
