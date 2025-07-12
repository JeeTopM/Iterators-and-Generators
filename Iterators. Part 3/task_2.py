"""
Функция is_iterable()
Реализуйте функцию is_iterable(), которая принимает один аргумент:
obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.
"""


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False


print(is_iterable(18731))
"""False"""

print(is_iterable("18731"))
"""True"""

objects = [(1, 13), 7.0004, [1, 2, 3]]
for obj in objects:
    print(is_iterable(obj))
"""
True
False
True
"""
