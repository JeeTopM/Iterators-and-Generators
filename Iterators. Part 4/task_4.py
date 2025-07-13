"""
Итератор Fibonacci
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.
Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.
"""


class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.second
        self.first, self.second = self.second, self.first + self.second
        return result


# Пример: 1
fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# ответ:
# 1
# 1
# 2
print()
# Пример: 2
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
# Ответ:
# 1
# 1
# 2
# 3
# 5
# 8
