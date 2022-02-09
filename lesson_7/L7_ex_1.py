import os

path_dict = {input('key>'): [input('val>') for i in range(int(input('count_val>')))]
             for j in range(int(input('count_key>')))}

for key, val in path_dict.items():
    for item in val:
        if not os.path.exists(os.path.join(key, item)):
            os.makedirs(os.path.join(key, item))

