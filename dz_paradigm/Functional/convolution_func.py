# Функция-редуктор: Напишите функцию-редуктор (или функцию свертки), которая принимает начальное значение и список чисел, а затем возвращает произведение всех чисел в списке. Используйте эту функцию для вычисления произведения чисел в списке.

def aply_func(numeric, func):
    return func(numeric)
    # return [func(x) for x in numeric]

def products_of_numbers(numeri):
    n = 1
    for el in numeri:
        n *= el
    return n

a = [1, 5 ,6 ,1 ,6 ,4 ,2]
b = [1, 2, 3]
print(aply_func(b, products_of_numbers))