class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(n) for n in l) for l in self.matrix) + '\n'

    def __add__(self, other):
        matr_s = Matrix([map(sum, zip(*line)) for line in zip(self.matrix, other.matrix)])
        return matr_s


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)
