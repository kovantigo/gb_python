import random
from random import randint

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом', 'школа', 'лодка']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью', 'утром']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

def get_jokes(n, flag=False):
    """
    Функция возвращает случайные шутки из трех списков слов
    :param n: количество шуток
    :param flag: True - генерирование опделенного количества шуток без повторений слов
    :return: список случайных шуток
    """
    joke_list = []
    if flag:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        for nou, adv, adj in zip(random.sample(nouns, n), adverbs, adjectives):
            joke_list.append(f'{nou} {adv} {adj}')
    else:
        count_jokes = randint(1, 100)
        print(f'Сгенерировано {count_jokes} шуток')
        for index in range(count_jokes):
            rand_nou = random.choice(nouns)
            rand_adv = random.choice(adverbs)
            rand_adj = random.choice(adjectives)
            joke_list.append(f'{rand_nou} {rand_adv} {rand_adj}')
    return joke_list

print(get_jokes(3, flag=False))
