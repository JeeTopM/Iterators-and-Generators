'''
Функция filterfalse()
Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает два аргумента:
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
iterable — итерируемый объект
Функция должна работать противоположно функции filter(), то есть возвращать итератор,
элементами которого являются элементы итерируемого объекта iterable, для которых функция predicate вернула значение False.
'''

def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: not predicate(x), iterable)

# 1
objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))
# 0 False []

# 2
numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))
# 1 3 5

# 3
numbers = [1, 2, 3, 4, 5]
print(*filterfalse(lambda x: x >= 3, numbers))
# 1 2