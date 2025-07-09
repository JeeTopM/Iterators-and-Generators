"""
Функция get_min_max() 😎
Реализуйте функцию get_min_max(), которая принимает один аргумент:
data — список произвольных объектов, сравнимых между собой
Функция должна возвращать кортеж, в котором первым элементом является индекс минимального элемента в списке data,
вторым — индекс максимального элемента в списке data. Если список data пуст, функция должна вернуть значение None.
"""


def get_min_max(data):
    if data:
        indexed_data = list(enumerate(data))
        min_data = min(indexed_data, key=lambda x: x[1])[0]
        max_data = max(indexed_data, key=lambda x: x[1])[0]
        return min_data, max_data
    else:
        return None

# 1
data = [2, 3, 8, 1, 7]
print(get_min_max(data))
# (3, 2)

# 2
data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))
# (0, 4)

# 3
data = [9]
print(get_min_max(data))
# (0, 0)
