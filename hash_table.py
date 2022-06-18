import hashlib

from typing import Any, List, Tuple, Optional


class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('----->', end=' ')
                print(data, end=' ')

            print()

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, item) -> Any:
        return self.get(item)


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num


if __name__ == '__main__':
    # hash_table = HashTable()
    # hash_table.add('car', 'Tesla')
    # hash_table.add('car', 'Toyota')
    # hash_table.add('pc', 'Mac')
    # hash_table.add('sns', 'Youtube')
    # # print(hash_table.table)
    # hash_table.print()
    # print(hash_table['sns'])
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))
    print(get_pair_half_sum(l))
