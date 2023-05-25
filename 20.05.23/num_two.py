# Создайте декоратор, повторяющий функцию заданное количество раз.

def Repeat(num: int):
    def decorator(func):
        for i in range(num):
            print(f"я повторилась {i + 1} раз")
            func()
    return decorator

@Repeat(5)
def Txxt():
    return print("Hellow, World!!")
