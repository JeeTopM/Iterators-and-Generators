"""
Функция random_numbers()
Реализуйте функцию random_numbers(), которая принимает два аргумента:
left — целое число
right — целое число
Функция должна возвращать итератор, генерирующий бесконечную последовательность
    случайных целых чисел в диапазоне от left до right включительно.
"""

from random import randint


def random_numbers(left, right):
    return iter(lambda: randint(left, right), None)


# 1
iterator = random_numbers(1, 1)
print(next(iterator))  # 1
print(next(iterator))  # 1
# 2
iterator = random_numbers(1, 10)
print(next(iterator) in range(1, 11))  # True
print(next(iterator) in range(1, 11))  # True
print(next(iterator) in range(1, 11))  # True
