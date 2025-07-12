"""
Функция is_iterator()
Реализуйте функцию is_iterator(), которая принимает один аргумент:
obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
"""


def is_iterator(obj):
    pass


# 1
print(is_iterator([1, 2, 3, 4, 5]))  # False
# 2
beegeek = map(str.upper, "beegeek")
print(is_iterator(beegeek))  # True
# 3
beegeek = filter(None, [0, 0, 1, 1, 0, 1])
print(is_iterator(beegeek))  # True
