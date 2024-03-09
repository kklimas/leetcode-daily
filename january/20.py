# todo in O(n)
def sum_subarray_mins(arr):
    n, result = len(arr), sum(arr)

    dynamic_arr = [[0 for _ in range(n)] if k != 0 else arr for k in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            dynamic_arr[i][j] = min(dynamic_arr[i - 1][j], dynamic_arr[i - 1][j + 1])
            result += dynamic_arr[i][j]
    return result % (10 ** 9 + 7)


n = [11, 81, 94, 43, 3]
print(sum_subarray_mins(n))
