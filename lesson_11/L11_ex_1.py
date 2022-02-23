from re import fullmatch, split

class Date:
    _MONTHS = {'january': ['01', 31], 'february': ['02', 28, 29], 'march': ['03', 31], 'april': ['04', 30],
              'may': ['05', 31], 'june': ['06', 30], 'july': ['07', 31], 'august': ['08', 31],
              'september': ['09', 30], 'october': ['10', 31], 'november': ['11', 30], 'december': ['12', 31]}

    @staticmethod
    def __validation(data):
        if fullmatch(r'\d{2}[./-]\w+[./-]\d{4}', data) == None:
            return False
        else:
            date_list = split(r'[./-]', data)
            if not date_list[1].isdigit():
                date_list[1] = Date.__month(date_list[1].lower())
            if Date.__correct_date(date_list):
                return date_list

    def __month(obj):
        for key in Date._MONTHS.keys():
            if obj == key:
                return Date._MONTHS[key][0]

    def __correct_date(obj):
        if int(obj[2]) % 4 == 0 and obj[1] == Date._MONTHS['february'][0] and int(obj[0]) <= Date._MONTHS['february'][2]:
            return True
        for value in Date._MONTHS.values():
            if int(obj[0]) <= value[1] and obj[1] == value[0]:
                return True
        raise ValueError(f'Даты не существует')

    @classmethod
    def type_data(cls, data):
        result = cls.__validation(data)
        if result == False:
            raise ValueError(f'Ошибка даты')
        else:
            return [int(i) for i in result]


try:
    date = '23-02-2021'
    date_list = Date.type_data(date)
    for item in date_list:
        print(item, type(item))
except ValueError as error:
    print(error)
