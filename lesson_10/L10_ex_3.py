class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, in_row):
        for i in range(self.nums // in_row):
            print('+' * in_row, end='\n')
        print('+' * (self.nums % in_row))
        return ''

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums - other.nums > 0:
            return Cell(self.nums - other.nums)
        else:
            raise ValueError(f'В первой клетке ячеек меньше, чем во второй')

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        return Cell(self.nums // other.nums)

    def __str__(self):
        return f'{self.nums}'

try:
    cell_1 = Cell(21)
    cell_2 = Cell(20)
    print(cell_1.make_order(4))
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 * cell_2)
    print(cell_1 // cell_2)
except ValueError as error:
    print(error)
