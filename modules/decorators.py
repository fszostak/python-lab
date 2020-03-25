#!/usr/bin/env python3

## fszostak(2020) Python 3.8 Code Snippets
#
#  Decorators

from functools import wraps

def repeat(_func=None, *, num_times=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    if _func is None:
        return decorator
    else:
        return decorator(_func)

class ClassRepeat(object):
    def __init__(self, num_times=2):
        self.num_times = num_times
       
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwarg):
            for _ in range(self.num_times):
                value = func(*args, **kwarg)
            return value
        return wrapper


