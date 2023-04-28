# Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в
# массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

masiv = [random.randint(0, 9) for i in range(15)]
print(masiv)
num = int(input("введите  число: "))
nw = []
while num > 0:
  nw.append(num % 10)
  num = num // 10
nw = nw[::-1]

res = True
for i in range(len(masiv)):
    if masiv[i] == nw[0]:
        count = 0
        j = 0
        while masiv[i] == nw[j] and i < len(masiv) - 1 and j < len(nw) - 1:
            i += 1 
            j += 1
            count += 1
        if count == 2:
            res = False
            print("да")
            break
if res:
    print("нет")
            