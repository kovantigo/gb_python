weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for item in weather:
    if (item.replace('+','').isdigit() or item.replace('-','').isdigit()) and weather[weather.index(item) - 1] != '"':
        weather.insert(weather.index(item), '"')
        weather.insert(weather.index(item) + 1, '"')
        if len(item) < 2:
            weather[weather.index(item)] = f'0{item}'
        elif len(item) == 2 and (ord(item[0]) == 43 or ord(item[0]) == 45):
            weather[weather.index(item)] = f'{item[0]}0{item[-1]}'

quot_mark = 0
for item in weather:
    if not(item.replace('+','').isdigit() or item.replace('-','').isdigit()) and item != '"':
        print(item, end=' ')
    elif item.replace('+','').isdigit() or item.replace('-','').isdigit():
        print(item, end='')
    elif item == '"' and quot_mark % 2 != 0:
        print(item, end=' ')
        quot_mark += 1
    else:
        print(item, end='')
        quot_mark += 1
