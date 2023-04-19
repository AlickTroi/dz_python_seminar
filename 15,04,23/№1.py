# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

n = abs(int(input("Введите число: ")))
count = 1
fibonachi = [1, 1]

for i in range(1, n - 1):
    count += fibonachi[i - 1]
    fibonachi.append(count)
    
print(fibonachi)
