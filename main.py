import telebot
from telebot import types
API_KEY = '6228897236:AAHQtrWqaIZjTtRJykbYQK87Ukv2VCYTc6w'
BOT = telebot.TeleBot(API_KEY)
class Actor():
    hp: [int, float] = 50
    damage: [int, float] = 10
    speed: [int, float] = 5
    armor: [int, float] = 0
    weapon: str = 'кулак'
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
class User():
    __state: [None, str] = None
    __name: str = 'Путник'
    __actor: object = Actor()
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

    @property
    def actor(self) -> object:
        return self.__actor

    @actor.setter
    def actor(self, actor: object) -> None:
        self.__actor = actor

class Mob():
    hp = 0
    def get_damage(self, damage):
        if damage > 0:
            self.hp -= damage
        return self.hp
class Goblin(Mob):
    name = 'Гоблин'
    hp = 30
    damage = 5
    speed = 7
    weapon = 'камень с дороги'
class Ogr(Mob):
    name = 'Огр'
    hp = 400
    damage = 20
    speed = 2
    weapon = 'большая дубина'

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
    pass
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





BOT.polling(none_stop=True, interval=0)


