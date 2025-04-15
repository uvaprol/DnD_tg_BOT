class Mob():
    hp = 0
    damage = 0
    def fight(self, damage):
        self.hp -= damage
        return self.damage if self.hp > 0 else 0
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