from numpy import round

class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return ComplexNumber(self.number + other.number)

    def __sub__(self, other):
        return ComplexNumber(self.number - other.number)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number)

    def __truediv__(self, other):
        if other.number == 0:
            raise ZeroDivisionError(f'Деление на нуль')
        return ComplexNumber(round(self.number / other.number, 2))

    def __str__(self):
        return f'{self.number}'

try:
    complex_1 = ComplexNumber(2 + 4j)
    complex_2 = ComplexNumber(1 + 3j)
    print(complex_1 + complex_2)
    print(complex_1 - complex_2)
    print(complex_1 * complex_2)
    print(complex_1 / complex_2)
except ZeroDivisionError as error:
    print(error)
