def read_file(start, end):
    with open('bakery.csv', 'r', encoding='utf-8') as r_file:
        if start > 0:
            for i in range(start - 1):
                r_file.readline()
        if end > start:
            for i in range(end - start + 1):
                yield r_file.readline().replace('\n','')
        elif end == 0:
            for i in r_file:
                yield i.replace('\n','')


if __name__ == "__main__":
    import sys

    start = end = 0
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        start = int(sys.argv[1])
    for file_str in read_file(start, end):
        print(f'{float(file_str)}')
