# Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.

print("Дроби: ")
list = []

for i in range (1,11):
    for n in range (2,12):
        list.append(i)
        list.append(n)
        if not int(list[0])//int(list[1]):
            if not (int(list[0]) % 2 == 0 and int(list[1]) % 2 == 0):
                if not (int(list[0]) % 3 == 0 and int(list[1]) % 3 == 0):
                    if not (int(list[0]) % 5 == 0 and int(list[1]) % 5 == 0):
                        print(f'{list[0]}/{list[1]}')
        list.clear()