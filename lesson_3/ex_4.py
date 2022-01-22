name_list = ['Иван Сергеев', 'Инна Серова', 'Илья Иванов', 'Петр Алексеев', 'Анна Савельева']

def thesaurus(*args):
    employees_dict = {}
    for employee in args:
        name, surname = employee.split()
        if not employees_dict.get(surname[0]):
            employees_dict[surname[0]] = {name[0]: [employee]}
        elif not employees_dict[surname[0]].get(name[0]):
            (employees_dict[surname[0]])[name[0]] = [employee]
        else:
            (employees_dict[surname[0]])[name[0]].append(employee)
    return employees_dict

print(thesaurus(*name_list))
