# Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей
# числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5

n = abs(int(input("Введите число: ")))
b = n
def Is_Int(a):
    return int(a) == a
def prime_number_count(n):
    list0 = []
    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1 
        if count == 2:
            list0.append(i)
    return list0

list0 = prime_number_count(n)
result_division = []
ind = 0

while n != 1:
    if Is_Int(n / list0[ind]):
        result_division.append(list0[ind])
        n =n / list0[ind]
    else:
        ind += 1

print(f"{b} -> {result_division} = {len(result_division)}")




