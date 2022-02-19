class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def dimension(self, matrix_1, matrix_2):
        for i in range(len(matrix_1)):
            if len(matrix_1[i]) != len(matrix_2[i]):
                return True

    def __str__(self):
        for i in self.matrix:
            for j in i:
                print(f'{j:3}', end='')
            print()
        return ''

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or self.dimension(self.matrix, other.matrix):
            raise ValueError(f'размерность матриц разная')
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] += other.matrix[i][j]
        return Matrix(self.matrix)

try:
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print(matrix_1 + matrix_2 + matrix_3)
except ValueError as error:
    print(error)
