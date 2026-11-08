import random

def generate_matrix(rows, cols):

    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(-100, 100))
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    if len(matrix2) != rows or len(matrix2[0]) != cols:
        return "Ошибка: Размерности матриц не совпадают!"
    result_matrix = []
    for i in range(rows):
        result_row = []
        for j in range(cols):
            sum_element = matrix1[i][j] + matrix2[i][j]
            result_row.append(sum_element)
        result_matrix.append(result_row)
        
    return result_matrix

def print_matrix(matrix, title):
    print(f"--- {title} ---")
    for row in matrix:
        print(row)
    print()

ROWS = 10
COLS = 10

matrix_1 = generate_matrix(ROWS, COLS)
matrix_2 = generate_matrix(ROWS, COLS)

matrix_3 = add_matrices(matrix_1, matrix_2)

print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")
print_matrix(matrix_3, "Матрица 3 (Результат сложения)")