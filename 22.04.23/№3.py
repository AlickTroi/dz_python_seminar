# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего
# совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов

# [1, 4, 2, 3, 6, 7]



a = [1, 4, 2, 3, 4, 6, 1, 7]
b = [1, 4, 2, 3, 6, 7]
a = set(a)
b = set(b)

result = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            count = 0
            while a[i] == b[j] and i < len(a) - 1 and j < len(b) - 1:
                i += 1 
                j += 1
                count += 1 
            if count > result:
                result = count
print(result)