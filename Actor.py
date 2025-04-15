from Mob import *
from random import choice
class Actor():
    hp: [int, float] = 50
    damage: [int, float] = 10
    speed: [int, float] = 5
    armor: [int, float] = 0
    weapon: str = 'кулак'
    town_target: bool = False
    __enemy: [None, object] = None
    __events: list = [['Встреча с гоблином', '', ''], ['Встреча с Огром', '', ''], ['Ни чего', '', '']]
    def lvlup(self):
        self.hp += self.hp / 10
    def get_damage(self):
        return self.damage
    def fight(self):
        damage = self.__enemy.fight(self.damage)
        self.hp -= damage
        return self.hp, self.__enemy.hp
    @property
    def event(self):
        return choice(self.__events)
    @property
    def enemy(self):
        return self.__enemy
    @enemy.setter
    def enemy(self, mob: object):
        self.__enemy = mob
