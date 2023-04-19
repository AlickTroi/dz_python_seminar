# Создайте скрипт бота, который находит ответы на фразы
# по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.



# import os.path
# scriptpath = os.path.dirname(__file__)
# filename = os.path.join(scriptpath, 'test.txt')
# data = open(filename, encoding='utf-8')
# text = data.readlines()
# bot = {}
# flag = True
# while flag: 
#     talk = input(": ")
#     if talk == "стоп":
#         data.close
#         print("ПОКА!")
#         flag = False
#     elif talk in text:
#         print(bot[talk])
#     else:
#         print("НеТ")



bot = {'как тебя зовут?': 'Ботя', 'выход': 'возвращайся еще:(\nСо словом не угадал:))))', 'привет': 'здравствуй', 'как дела': 'норм'}

flag = True
while flag: 
    talk = input(": ")
    if talk == "стоп":
        print("ПОКА!")
        flag = False
    elif talk in bot:
        print(bot[talk])
    else:
        print("НеТ")



