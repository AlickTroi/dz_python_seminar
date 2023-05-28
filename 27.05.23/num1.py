# Задача 1. Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.

import numpy as np

el = np.random.randint(0, 10, 15)
print(el)

unique_list, uniq_count = np.unique(el, return_counts=True)

count = 0 
print(unique_list)
print(uniq_count)
for i in uniq_count:
    if i == 1:
        count += 1
print(f"количество уникальных элементов = {count}")