"""
Итератор BoundedRepeater
Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает два аргумента в следующем порядке:
obj — произвольный объект
times — натуральное число
Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать исключение StopIteration.
"""


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times == 0:
            raise StopIteration
        self.times -= 1
        return self.obj


# 1
bee = BoundedRepeater("bee", 2)
print(next(bee))
print(next(bee))
"""
bee
bee
"""

# 2
geek = BoundedRepeater("geek", 3)
print(next(geek))
print(next(geek))
print(next(geek))
try:
    print(next(geek))
except StopIteration:
    print("Error")
"""
geek
geek
geek
Error
"""
