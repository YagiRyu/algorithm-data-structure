import time

from typing import List
from collections import Counter


def memoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return _wrapper


@memoize
def long_func(num: int) -> int:
    r = 0
    for i in range(100000000):
        r += num * i
    return r


def min_count_remove(x: List[int], y: List[int]) -> None:
    count_x = Counter(x)
    count_y = Counter(y)

    for key_x, value_x in count_x.items():
        value_y = count_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = {i for i in x if i != key_x}
            elif value_x > value_y:
                y[:] = {i for i in y if i != key_x}


if __name__ == '__main__':
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print('x = ', x)
    print('y = ', y)
    min_count_remove(x, y)
    print('x = ', x)
    print('y = ', y)

