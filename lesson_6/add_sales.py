def add_file(cash):
    with open('bakery.csv', 'a', encoding='utf-8') as w_file:
        for i in cash:
            w_file.write(f'{i}\n')


if __name__ == "__main__":
    import sys

    name, *cash = sys.argv
    add_file(cash)
