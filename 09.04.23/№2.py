#Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"|{x}| |{y}| |{z}| |{int(not(x and y) or z)}|")