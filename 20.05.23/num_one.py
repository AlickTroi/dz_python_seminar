# Создайте пользовательский аналог метода map().

def Same_as_map(func, listt):
    return [func(el) for el in listt]

num = (0, 3, 5, 0, 5, 7)

print(list(map(lambda x: x + 11, num)))

print(list(Same_as_map(lambda x: x + 11, num)))