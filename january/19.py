def min_falling_path_sum(matrix):
    n = len(matrix)
    dynamic_matrix = [[0 for _ in range(n)] if i != 0 else matrix[0] for i in range(n)]
    for i in range(1, n):
        for j in range(n):
            if 0 < j < n - 1:
                block_val = min(dynamic_matrix[i - 1][j - 1], dynamic_matrix[i - 1][j], dynamic_matrix[i - 1][j + 1])
            elif j > 0:
                block_val = min(dynamic_matrix[i - 1][j - 1], dynamic_matrix[i - 1][j])
            else:
                block_val = min(dynamic_matrix[i - 1][j + 1], dynamic_matrix[i - 1][j])

            if i == 2 and j == 0:
                print(block_val, matrix[i][j])
            dynamic_matrix[i][j] = block_val + matrix[i][j]

    return min(dynamic_matrix[n - 1])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(min_falling_path_sum(matrix))
