import telebot
from telebot import types
from User import *
API_KEY = '6228897236:AAHQtrWqaIZjTtRJykbYQK87Ukv2VCYTc6w'
BOT = telebot.TeleBot(API_KEY)

users: dict = {}
@BOT.message_handler(commands=['start'])
def start_message(message):
    global users
    USER_ID = message.from_user.id
    users.update({USER_ID: User()})
    users[USER_ID].state = 'name_reg'
    BOT.send_message(USER_ID, 'Приветствую путешественник, назови свое имя:')

@BOT.message_handler(commands=['get_name'])
def get_name(message):
    global users
    USER_ID = message.from_user.id
    user_name = users[USER_ID].name
    BOT.send_message(USER_ID, user_name)
@BOT.callback_query_handler(func=lambda call: call.data == 'start_game')
def start_game(message):
    USER_ID = message.from_user.id
    users[USER_ID].actor = Actor()
    BOT.send_message(USER_ID, f'{users[USER_ID].name}, ваше путешествие начинается')
    keyboard = types.ReplyKeyboardMarkup()
    button_go = types.KeyboardButton(text="Путешествовать")
    button_town = types.KeyboardButton(text="Вернуться")
    keyboard.add(button_go, button_town)
    users[USER_ID].state = 'in_game'
@BOT.callback_query_handler(func=lambda call: call.data == 'repeat')
def repeat(message):
    USER_ID = message.from_user.id
    keyboard = types.InlineKeyboardMarkup()
    button_y = types.InlineKeyboardButton(text="Я готов", callback_data='start_game')
    button_n = types.InlineKeyboardButton(text="Изменить имя", callback_data='change_name')
    keyboard.add(button_y, button_n)
    BOT.send_message(USER_ID, f'{users[USER_ID].name}, вернись когда будешь готов', reply_markup=keyboard)
@BOT.message_handler(content_types=['text'])
def message_validator(message):
    global users
    USER_ID = message.from_user.id
    if users[USER_ID].state == 'name_reg':
        users[USER_ID].name = message.text
        keyboard = types.InlineKeyboardMarkup()
        button_y = types.InlineKeyboardButton(text="Да", callback_data='start_game')
        button_n = types.InlineKeyboardButton(text="Нет", callback_data='repeat')
        keyboard.add(button_y, button_n)
        BOT.send_message(USER_ID, f'{message.text}, хочешь ли ты начать путешествие', reply_markup=keyboard)
    elif users[USER_ID].state == 'in_game':
        def get_event() -> None:
            text, opt1, opt2 = users[USER_ID].event
            if not (opt1 == opt2 == ''):
                keyboard = types.InlineKeyboardMarkup()
                button_y = types.InlineKeyboardButton(text="opt1", callback_data='opt1')
                button_n = types.InlineKeyboardButton(text="opt2", callback_data='opt2')
                keyboard.add(button_y, button_n)
                BOT.send_message(USER_ID, text, reply_markup=keyboard)
            else:
                BOT.send_message(USER_ID, text)
        if message.text == 'Путешествовать':
            get_event()
        elif message.text == 'Вернуться':
            users[USER_ID].actor.town_target = True
            get_event()






BOT.polling(none_stop=True, interval=0)


