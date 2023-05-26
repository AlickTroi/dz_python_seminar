# Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.

import telebot

bot = telebot.TeleBot(token)

answer_for_offer = open("offer.txt", mode="r", encoding="utf-8")
data = answer_for_offer.readlines()
answer_for_offer.close()
data = list(el[:-1] for el in data)
for i in data:
    el = i.split(":")
    print(el[1])
    answer = input("Введите ответ: ")
    bot.send_message(el[0], f"Вы ввели предложенние {el[1]}! \n Наш ответ: {answer}! \n Спасибо за обращенние!")
answer_for_offer = open("offer.txt", mode="w", encoding="utf-8")
answer_for_offer.write("")
answer_for_offer.close()