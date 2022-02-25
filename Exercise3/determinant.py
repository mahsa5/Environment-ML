#program to find a matrix determinant

mat = [[1, 0, 2],

           [3, 0, 4],

           [5, 1, 6]]

        

def get_factor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def determinant(mat):
    if(len(mat) == 2):
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
    Sum = 0
    for column in range(len(mat)):
        sign = (-1) ** (column)
        sub_det = determinant(get_factor(mat, 0, column))
        Sum += (sign * mat[0][column] * sub_det)
    return Sum

print('Determinant of the matrix is :', determinant(mat))







