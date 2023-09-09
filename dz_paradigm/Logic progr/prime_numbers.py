# Простые числа - это числа больше 1, которые не имеют делителей, кроме 1 и самих себя. Задача состоит в том, чтобы написать программу, которая будет находить и выводить все простые числа в заданном диапазоне.

def is_prime_number(num: int):
    count = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def search_prime_number(first_num: int, last_num: int):
    result = []
    while first_num <= last_num:
        if is_prime_number(first_num):
            result.append(first_num)
        first_num += 1
    return result

a = search_prime_number(3, 101)
print(a)