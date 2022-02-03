import collections

with open('ex1w.txt', 'w', encoding='utf-8') as w_file:
    with open('ex1r.txt', 'r', encoding='utf-8') as r_file:
        w_file.writelines((f'{item.split()[0]}\n' for item in r_file))

with open('ex1w.txt', 'r', encoding='utf-8') as r_file:
    print(collections.Counter(r_file.readlines()).most_common(1)[0][0].replace('\n', ''))
