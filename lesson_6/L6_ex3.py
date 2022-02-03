from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as r_file:
    users = [user.replace(',',' ').replace('\n','') for user in r_file]

with open('hobby.csv', 'r', encoding='utf-8') as r_file:
    hobby = [hobby.replace('\n','') for hobby in r_file]

if len(users) > len(hobby):
    users_hobby_dict = dict(zip_longest(users, hobby, fillvalue=None))
    with open('users_hobby.txt', 'w', encoding='utf-8') as w_file:
        w_file.writelines(f'{user} - {hobby}\n' for user, hobby in users_hobby_dict.items())
else:
    exit(1)
