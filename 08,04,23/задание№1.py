# Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели

number_week = int(input("Введите число дня недели: "))

if number_week == 1:
    print("Понедельник")
elif number_week == 2:
    print("Вторник")
elif number_week == 3:
    print("Среда")
elif number_week == 4:
    print("Четверг")
elif number_week == 5:
    print("Пятница")
elif number_week == 6:
    print("Суббота")
elif number_week == 7:
    print("Воскресенье")
else :
    print("такого дня нет")
