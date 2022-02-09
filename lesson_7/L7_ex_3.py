from os import walk
from os.path import join, split
from shutil import copytree

try:
    all_files = {f'{root}' for root, dirs, files in walk('my_project') if f'{root}'.find('templates\\') != -1}
    for link in all_files:
        copytree(link, join(r'my_project\templates', split(link)[1]))
except FileExistsError:
    print('Файлы перенесены')
