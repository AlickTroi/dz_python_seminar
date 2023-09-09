# Замыкание: Создайте функцию, которая принимает некоторое число n и возвращает функцию, которая прибавляет n к своему аргументу. Продемонстрируйте использование этой функции-замыкания.

def aply_func(func, num, num1):
    return func(num) + num1

def products_of_numbers(numeri):
    n = 1
    for el in numeri:
        n *= el
    return n

a = [1, 5 ,6 ,1 ,6 ,4 ,2]
b = [1, 2, 3]
print(aply_func( products_of_numbers, b, 7))