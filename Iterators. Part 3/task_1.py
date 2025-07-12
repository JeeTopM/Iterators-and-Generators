"""
Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор,
бесконечно генерирующий единственное значение — строку i love beegeek!.
"""

infinite_love = iter(lambda: "i love beegeek!", None)

# 1
print(next(infinite_love))
# i love beegeek!
print() # просто пробел
# 2
print(next(infinite_love))
print(next(infinite_love))
print(next(infinite_love))
"""
i love beegeek!
i love beegeek!
i love beegeek!
"""
