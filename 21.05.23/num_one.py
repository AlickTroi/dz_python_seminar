# Напишите бота для техподдержки. 
# Бот должен записывать обращения пользователей в файл.


import telebot


bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: message.text.lower() == "предложение" )
def offer_log(message):
    bot.send_message(message.chat.id, "Введите ваше обращение: ")
    bot.register_next_step_handler(message, offer)

def offer(message):
    data = open("offer.txt", mode="a", encoding="utf-8")
    text = f"{message.from_user.id} : {message.text} \n"
    data.write(text) 
    data.close()

bot.polling()