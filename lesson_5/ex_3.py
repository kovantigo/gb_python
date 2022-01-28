from itertools import islice
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ксения', 'Антон', 'Игорь', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klasses.extend([None for item in range(len(tutors) - len(klasses))])
school = (name for name in zip(tutors, klasses))
print(*islice(school, len(tutors)))
