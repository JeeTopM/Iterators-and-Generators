"""
Итератор DictItemsIterator
Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:
data — словарь
Итератор класса DictItemsIterator должен генерировать последовательность кортежей,
представляющих собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.
"""


class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.iter = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.iter)
        value = self.data[key]
        return (key, value)


# 1
pairs = DictItemsIterator({1: "A", 2: "B", 3: "C"})
print(*pairs)
# (1, 'A') (2, 'B') (3, 'C')

# 2
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
pairs = DictItemsIterator(data)
print(*pairs)
# (1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49)
