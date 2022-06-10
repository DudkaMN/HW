class Cell:

    def __init__(self, cell):
        if cell <= 0:
            print('В клетке должна быть как минимум 1 ячейка')
        else:
            self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell < other.cell:
            print('Первая клетка должна быть больше второй')
        else:
            return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    @property
    def make_order(self):
        print(('*****'+'\n') * (self.cell // 5) + '*' * (self.cell % 5) + '\n')


c_1 = Cell(25)
c_2 = Cell(16)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
c_1.make_order
c_2.make_order
