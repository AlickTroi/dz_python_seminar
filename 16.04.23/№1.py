# Дано натуральное число N. Напишите метод,
# который вернёт список простых множителей
# числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5


n = abs(int(input("Введите число: ")))

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

# def counting_prime_number_in_list(n, list0 : list):
#     lis = []
#     ind = 0
#     while n >= 0: 
#         if n % list[ind] == 0:
#             lis.append(list[ind])
#             n /= 2
#         else:
#             ind += 1
#     return lis

list0 = prime_number_count(n)


result_division = []
ind = 0
while n >= 0: 
    if n % int(list0[ind]) == 0:
        result_division.append(list0[ind])
        n /= 2
    # else:
    #     ind += 1

print(result_division)

