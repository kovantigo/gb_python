name_list = ['Евдокия', 'Галина', 'Евгений', 'Елена', 'Игорь', 'Анастасия', 'Иван', 'Антон', 'Ксения']
names_of_employees = {}

def thesaurus(*args):
    for item in list(args):
        name_values = list(filter(lambda name: name.title().startswith(item[0]), args))
        name_values.sort()
        names_of_employees.setdefault(item[0], name_values)
        sorted_tuple = dict(sorted(names_of_employees.items(), key=(lambda tuple_item: tuple_item[0])))
    return sorted_tuple

print(thesaurus(*name_list))
