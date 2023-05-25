import requests
import telebot
import random
import time

bot = telebot.TeleBot("Token")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "How are you doing?")

find_num = random.randint(0, 1000)

@bot.message_handler(func=lambda message: message.text.lower() == "игра")
def game_find_number(message):
    bot.send_message(message.from_user.id, "игра началась!!!")
    count = 0
    global find_num
    find_num = random.randint(0, 1000)
    bot.register_next_step_handler(message, game_pro)
    
def game_pro(message):   
    text = message.text
    if text == "сдаюсь":
        bot.send_message(message.from_user.id, f"Вы были близки. Вы сделали  попытки,  загаданно было число {find_num}")
        return 
    elif not text.isdigit():
        bot.send_message(message.chat.id, "Вы ввели не число")
        bot.send_message(message.from_user.id, "для выхода напишите |сдаюсь|")
        bot.register_next_step_handler(message, game_pro)

    if int(text) == find_num:
        bot.send_message(message.from_user.id, f"Поздравляю!!!{find_num} число найденно!!! Вы победили!!!")
        req = requests.get(f'https://cataas.com/cat?{time.time()}')
        return
    elif int(text) < find_num:
        bot.send_message(message.from_user.id, "Ваше число меньше искомого")
        bot.register_next_step_handler(message, game_pro)
    elif int(text) > find_num:
        bot.send_message(message.from_user.id, "Ваше число больше искомого")
        bot.register_next_step_handler(message, game_pro)

bot.polling()