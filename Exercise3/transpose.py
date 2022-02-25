#program to find a matrix transpose

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
def matrix_transpose(matrix):
    if not matrix: 
        return []
    else:
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix_transpose(matrix))
