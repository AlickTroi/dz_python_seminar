# Напишите программу, которая принимает на
# вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.

point_one_x = int(input("Введите X первой точки: "))
point_one_y = int(input("Введите Y первой точки: "))

point_two_x = int(input("Введите X первой точки: "))
point_two_y = int(input("Введите Y первой точки: "))

decision = (((point_one_x - point_two_x)**2)+((point_one_y - point_two_y)**2))**0.5
print(decision)