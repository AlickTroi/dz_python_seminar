# Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random


i = [random.randint(0, 10) for i in range(25)]
print(i)

j = list(filter(lambda x: x > 5, i))

print(j)