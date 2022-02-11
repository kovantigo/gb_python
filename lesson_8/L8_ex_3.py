from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        my_list = [item for item in args]
        my = [f'{func.__name__}({item}: {type(item)})' for item in my_list]
        print(*my, *func(*args), sep='\n')
    return wrapper

@type_logger
def calc_cube(*num):
    my_list = [item for item in num if isinstance(item, int) or isinstance(item, float)]
    return [round(i ** 3, 2) for i in my_list]

calc_cube(3, 4.1, {'key': 1})
