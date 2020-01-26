from datetime import datetime
from functools import wraps
from time import time


def log_run(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        date = datetime.now()
        super_string = date.strftime("%Y/%m/%dT%H:%M:%S")

        klucze = kwargs.keys() if len(kwargs) else "-"

        start = time()
        ret = fun(*args, **kwargs)
        end = time()
        diff = end-start

        print(f"{super_string}| function {fun.__name__} called with:")
        print(f"{len(args)} positional parameters.")
        print(f"optionl parameters: {klucze}")
        print(f"returned: {ret} ({diff:.2e}s)")
        return ret

    return wrapper
@log_run
def fun(*args, **kwargs):
    pass


if __name__ == '__main__':
    decorated_sum = log_run(sum)
    decorated_sum([1,2,3])
    fun(1, 2, 'a', bb=1)
    # Przykładowy log
    # 2020-01-23T21:09:55| function sum called with:
    # 1 postional parameters
    # optional parameters: -
    # returned: 6 (1.43e-06s)
    # 2020-01-23T21:09:55| function fun called with:
    # 3 postional parameters
    # optional parameters: bb
    # returned: None (1.43e-06s)
