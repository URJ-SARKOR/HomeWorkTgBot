import telebot , button_help

bot = telebot.TeleBot('6515352041:AAFQNzr_ftz6K8rP6Mw2Zsj3-BImCbYi9jE')

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,'Выберите Действия', reply_markup=(button_help.button_help()))


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Если у вас есть проблемы напишите нашему БОССУ его контак:@White_Lotus_9474')
    bot.register_next_step_handler(message,help)


bot.polling(none_stop=True)
