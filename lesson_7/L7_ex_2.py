import yaml
import os

def path_name(object, root):
    if isinstance(object, dict):
        for key, value in object.items():
            new_root = os.path.join(root, key)
            os.makedirs(new_root)
            path_name(value, new_root)
    elif isinstance(object, list):
        for item in object:
            path_name(item, root)
    else:
        new_root = os.path.join(root, object)
        with open(new_root, 'w', encoding='utf-8') as file:
            file.write('')

with open('config.yaml', 'r', encoding='utf-8') as r_file:
    path_dict = yaml.load(r_file, Loader=yaml.FullLoader)

    for root, value in path_dict.items():
        path_name(value, root)
