# Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.

pov = int(input("введите количество повторов: "))
n = str(input("введите число: "))
result = 0
for i in range(1, pov + 1):
    result += int(n * i)
print(result)










