def find_max_min_indices(matrix):
    flat_matrix = [element for row in matrix for element in row]
    max_index = flat_matrix.index(max(flat_matrix))
    min_index = flat_matrix.index(min(flat_matrix))
    num_cols = len(matrix[0])
    return min_index // num_cols, min_index % num_cols, max_index // num_cols, max_index % num_cols

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

min_row, min_col, max_row, max_col = find_max_min_indices(matrix)
print("Найменший елемент знаходиться у рядку", min_row+1, "і стовпці", min_col+1)
print("Найбільший елемент знаходиться у рядку", max_row+1, "і стовпці", max_col+1)
