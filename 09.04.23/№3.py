# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = list(set(input("Введте первое слово: ")))
str2 = input("Введте второе слово: ")

for i in str1:
    count = 0
    for j in str2:
        if j == i:
            count += 1
    print(f" символ {i} встречался {count} раз")