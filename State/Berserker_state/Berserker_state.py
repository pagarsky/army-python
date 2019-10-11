from Unit.Unit import *
from config.config import *


class Berserker_state(State):

    def __init__(self, name : str, hp : int, dmg : int):
        State.__init__(name, hp, dmg)

    def take_damage(self, dmg : int):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        else:
            self.dmg += 10


    def take_magic_damage(self, dmg : int):
        pass