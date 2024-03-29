import Unit
from exceptions import *

class Ability:

    def __init__(self, owner):
        self.owner = owner

    def attack(self, enemy : Unit):
        if enemy is self.owner:
            raise AttacksItself()
        if not self.owner.is_alive():
            raise CantDoCauseDead(self.owner)
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg)
            enemy.counter_attack(self.owner)
        else:
            raise TargetIsDead()

    def counter_attack(self, enemy : Unit):
        if not self.owner.is_alive():
            raise CantDoCauseDead(self.owner)
        if enemy.is_alive():
            enemy.take_damage(self.owner.dmg // 2)
        else:
            raise TargetIsDead()