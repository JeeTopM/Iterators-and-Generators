"""
Итератор Square
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:
n — натуральное число,
Итератор класса Square должен генерировать последовательность из n чисел,
каждое из которых является квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.
"""


class Square:
    def __init__(self, n):
        self.n = n
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.cnt:
            raise StopIteration
        self.cnt += 1
        return self.cnt**2


# 1
squares = Square(2)
print(next(squares))
print(next(squares))
"""
1
4
"""
# 2
squares = Square(10)
print(list(squares))
"""
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
# 3
squares = Square(1)
print(list(squares))
"""
[1]
"""
