# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

n = abs(int(input("Введите Н: ")))

array = []
shift = int(input("Введите число(сдвиг): "))

for i in range(-n, n + 1, 1):
    array.append(i)

array = array[-shift:] + array[:-shift]

print(array)

