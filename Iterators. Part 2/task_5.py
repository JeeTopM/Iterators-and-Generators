"""
Функция get_min_max() 😳
Реализуйте функцию get_min_max(), которая принимает один аргумент:
iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable,
    вторым — максимальный элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст,
    функция должна вернуть значение None.
"""


def get_min_max(iterable):
    pass


# 1
iterable = iter(range(10))
print(get_min_max(iterable))
# (0, 9)

# 2
iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))
# (1, 33)

# 3
iterable = iter([])
print(get_min_max(iterable))
# None
