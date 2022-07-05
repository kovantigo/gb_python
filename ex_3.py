category_of_units_1 = [5,6,7,8,9,0]
category_of_units_2 = [2,3,4]
for number in range(101):
    if number % 10 == 1 and number != 11:
        print(number, 'процент')
    if number % 10 in category_of_units_2 and (number < 12 or number > 14):
        print(number, 'процента')
    if number % 10 in category_of_units_1 or (number >= 11 and number <= 14):
        print(number, 'процентов')
