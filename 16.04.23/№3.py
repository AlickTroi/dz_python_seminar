# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142

import math
n = float(input("Введите до чего округлять: "))
 
count = 0
while n < 1:
    n *= 10
    count += 1
    
print(round(math.pi, count))

