def unique_occurrences(arr):
    occurrences = [0 for _ in range(2000)]
    for num in arr:
        occurrences[num + 1000] += 1
    occurrences_diff_zero = [k for k in occurrences if k != 0]
    return len(occurrences_diff_zero) == len(set(occurrences_diff_zero))
