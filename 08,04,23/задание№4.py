# Напишите программу, которая на вход
# принимает число (N), а на выходе показывает все чётные
# числа от 1 до N.

num = int(input("Введите число: "))
count = 1

if num > 0:
    while count <= num:
        if count % 2 == 0 or count == 1 or count == num:
            print(count)
        count += 1
else :
    while count >= num:
        if count % 2 == 0 or count == 1 or count == num:
            print(count)
        count -= 1
