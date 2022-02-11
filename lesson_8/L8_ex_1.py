from re import fullmatch, split

def email_parse(email):
    if fullmatch(r"[\w.-]+@[\w]+.[\w]+", email) == None:
        raise ValueError
    else:
        parts_email = split(r"@", email)
        print({'username': parts_email[0], 'domain': parts_email[1]})


try:
    email_parse(input('Введите адрес>>'))
except ValueError:
    print('Неверный адрес')
