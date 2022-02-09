import django
from os import walk
from os.path import getsize, splitext

my_dict = {}
file_structure = django.__path__[0]

for root, dirs, files in walk(file_structure):
    for item in files:
        link = rf'{root}\{item}'
        if splitext(link)[1] != '':
            key = 10 ** len(str(getsize(link)))
            extension = link.rsplit('.')[-1]
            if my_dict.get(key, None):
                my_dict[key][0] += 1
                if extension not in my_dict[key][1]:
                    my_dict[key][1].append(extension)
            else:
                my_dict[key] = [1, [extension]]

my_dict = dict(sorted(my_dict.items(), key=lambda i: i[0], reverse=True))
print(my_dict)
