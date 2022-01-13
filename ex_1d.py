duration = int(input('Введите время в секундах>>'))

time = []
time_name = ['дн', 'час', 'мин', 'сек']

days = duration // (60 ** 2 * 24)
time.append(days)
duration -= days * (60 ** 2 * 24)
hours = duration // (60 ** 2)
time.append(hours)
duration -= hours * (60 ** 2)
minutes = duration // 60
time.append(minutes)
duration -= minutes * 60
time.append(duration)

for index in range(len(time)):
    if time[index] > 0:
        print(time[index], time_name[index], end=' ')
