from functools import wraps

def val_checker(lambda_func):
    def real_checker(func):
        @wraps(func)
        def wrapper(x):
            if lambda_func(x):
                print(func(x), type(func(x)), end='\n')
            else:
                raise ValueError
        return wrapper
    return real_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

try:
    calc_cube(-5)
except ValueError:
    print('Ошибка')
