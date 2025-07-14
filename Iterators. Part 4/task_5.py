"""
Итератор PowerOf
Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:
number — ненулевое число
Итератор класса PowerOf должен генерировать бесконечную последовательность целых
    неотрицательных степеней числа number в порядке возрастания, начиная с нулевой степени.
"""


class PowerOf:
    def __init__(self, number):
        self.number = number
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = pow(self.number, self.cnt)
        self.cnt += 1
        return result


# Пример:
power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
# Ответ:
# 1
# 2
# 4
# 8
