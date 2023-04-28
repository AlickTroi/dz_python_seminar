# Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

num = [random.randint(0, 10) for _ in range(25)]
print(num)

result = []
for j in range(0,len(num)):
    for i in range(j,len(num)):
        if i ==j:
            result.append(num[i])
        elif num[i] > result[-1]:
            result.append(num[i])
    if len(result) != 1:
        print(result)
        result.clear()