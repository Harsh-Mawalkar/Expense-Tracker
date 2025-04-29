import functools
import datetime

def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Function '{func.__name__}' was called")
        return func(*args, **kwargs)
    return wrapper
