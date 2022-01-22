numerals = {'zero': 'нуль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(numeral):
    if (numeral.lower() in numerals) and numeral.istitle():
        return numerals.get(numeral.lower()).title()
    else:
        return numerals.get(numeral)

numeral = input('Введите числительное>>')
print(num_translate(numeral))
