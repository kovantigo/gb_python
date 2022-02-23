from re import sub, search

class Error(Exception):
    def __init__(self, text):
        self.__text = text

class ListOfNumbers:
    list_numb = []

    def input_numb(self):
        while True:
            try:
                try:
                    number = input('Введите число или stop для окончания ввода>>').lower()
                    if number == 'stop':
                        return ListOfNumbers.list_numb
                    elif not sub(r'[.,]', '', number).isdigit():
                        raise Error(f'Ввели не число')
                    elif search(r'[.,]', number) != None:
                        ListOfNumbers.list_numb.append(float(sub(r',', '.', number)))
                    else:
                        ListOfNumbers.list_numb.append(int(number))
                except Error as error:
                    print(error)
            except Exception:
                self.input_numb()


a = ListOfNumbers()
b = a.input_numb()
print(b)
