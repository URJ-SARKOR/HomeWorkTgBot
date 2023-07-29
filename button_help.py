from telebot import types
def button_help():
    kb = types.ReplyKeyboardMarkup()

    button_help = types.KeyboardButton('/help')

    kb.add(button_help)

    return kb