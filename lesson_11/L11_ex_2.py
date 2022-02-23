class Error(Exception):
    def __init__(self, text):
        self.__text = text

def division():
    try:
        dividend, divider = map(int, input('Введите делимое и делитель>>').split())
        if divider == 0:
            raise Error(f'Делитель равен нулю. Деление невозможно!')
        else:
            quotient = round(dividend / divider, 2)
            return quotient
    except ValueError:
        return f'Ввели не число'
    except Error as error:
        return error


print(division())
