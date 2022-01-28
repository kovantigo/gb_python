from requests import get
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

my_list = response.split('</Value>')
day, month, year = map(int, response.split('Date')[1].split('"')[1].split('.'))

def currency_rates(currency):
    for item in my_list:
        if item.find(currency) != -1:
            ex_rate = float(item.split('<Value>')[1].replace(',', '.'))
            return f'{date(year, month, day)}\n{currency}\n{ex_rate}'

currency = input('Введите валюту>>').upper()
print(currency_rates(currency))