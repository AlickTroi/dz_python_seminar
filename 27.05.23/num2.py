# Задача 2. Создайте двумерный массив, размером 5х5. Определите, 
# есть ли в нём одинаковые строки.

import numpy as np

arr1 = np.random.randint(0, 10, (5, 5))
print(arr1)
count = 0
for i in range(5):
    for j in range(i, 5):
        result = np.array_equal(arr1[i], arr1[j], equal_nan="False")
        if i != j and result:
            print(f"совпадают строки {i + 1} {j + 1}")
            count = 1
if count == 0:
    print("совпадений нет")
    



