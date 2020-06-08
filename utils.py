import time
from functools import wraps
from pathlib import Path


def read_file(name, *, do_strip=True):
    path = Path(f'/Users/sschwa12/code/aoc2016/inputs')
    if isinstance(name, int):
        name = f'{name:02d}'
    with open(path / name) as f:
        res = f.readlines()
    if do_strip:
        res = list(map(str.strip, res))
    return res


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f'{func.__name__!r} took {time.perf_counter() - start} seconds')

    return wrapper
