import telebot
from telebot import types
API_KEY = '6228897236:AAHQtrWqaIZjTtRJykbYQK87Ukv2VCYTc6w'
BOT = telebot.TeleBot(API_KEY)

class User():
    def __init__(self) -> None:
        self.__name: [None, str] = None
        self.__state: [None, str] = None

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str) -> None:
        self.__state = state

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

class Actor():
    hp: [int, float] = 50
    damage: [int, float] = 10
    speed: [int, float] = 5
    armor: [int, float] = 0
    weapon: str = 'arm'
    def __init__(self, name):
        self.__name = name
    def lvlup(self):
        self.hp += self.hp / 10
    def set_equipment(self, weapon, damage, armor=0):
        self.weapon = weapon
        self.damage = damage
        self.armor = armor
    def get_hp(self):
        return self.hp + self.armor
    def get_damage(self, damage):
        if damage > 0:
            self.hp -= damage
            return self.hp
     
class Mob():
    def __init__(self, name, hp, damage, speed, weapon):
        self.name = name
        self.hp: [int, float] = hp
        self.damage: [int, float] = damage
        self.speed: [int, float] = speed
        self.weapon: str = weapon
    def get_damage(self, damage):
        if damage > 0:
            self.hp -= damage
            return self.hp

ogr = Mob('Огр', 400, 20, 2, 'Большая дубина')
goblin = Mob('Гоблин', 30, 5, 7, 'Камень с дороги')

users: dict = {}
@BOT.message_handler(commands=['start'])
def start_message(message):
    global users
    USER_ID = message.from_user.id
    users.update({USER_ID: {'user': User()}})
    users[USER_ID]['user'].state = 'name_reg'
    BOT.send_message(USER_ID, 'Приветствую путешественник, назови свое имя:')

@BOT.message_handler(commands=['get_name'])
def get_name(message):
    global users
    USER_ID = message.from_user.id
    user_name = users[USER_ID]['user'].name
    BOT.send_message(USER_ID, user_name)

@BOT.message_handler(content_types=['text'])
def message_validator(message):
    global users
    USER_ID = message.from_user.id
    if users[USER_ID]['user'].state == 'name_reg':
        users[USER_ID]['actor'] = Actor(message.text)
        users[USER_ID]['actor'].name = message.text
        # BOT.send_message(USER_ID, f'Приветствую {message.text}')
        users[USER_ID]['user'].state = 'get_ready'
        keyboard = types.InlineKeyboardMarkup()
        button_y = types.InlineKeyboardButton(text="Да", callback_data='y')
        button_n = types.InlineKeyboardButton(text="Нет", callback_data='n')
        keyboard.add(button_y, button_n)
        BOT.send_message(USER_ID, f'{message.text}, хочешь ли ты начать путешествие', reply_markup=keyboard)





BOT.polling(none_stop=True, interval=0)


