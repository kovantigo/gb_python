pos_employee = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                'товарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for item in pos_employee:
    pos_emp_parts = item.split()
    name_emp = pos_emp_parts[-1].title()
    print(f'Привет, {name_emp}!')
