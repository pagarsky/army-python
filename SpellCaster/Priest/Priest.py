from SpellCaster.SpellCaster import SpellCaster
from Spell import Fireball, Heal, Blessing
from config import *


class Priest(SpellCaster):

    def __init__(self, name : str = "Priest",
                 hp : int = Hp.PRIEST_HP.value,
                 mp : int = Mp.PRIEST_MP.value,
                 dmg : int = Dmg.PRIEST_DMG.value):
        SpellCaster.__init__(self, name, hp, mp, dmg)
        self.spellbook.add(
            Fireball.Fireball(SpellDmg.FIREBALL_DMG.value//2),
            Blessing.Blessing(),
            Heal.Heal()
        )

    def cast_spell(self, spell, target):
        if target.type == "undead":
            spl = getattr(self.spellbook, spell)
            spl.dmg *= 2
            self.magic_ability.cast_spell(spl, target)
            spl.dmg /= 2
        else:
            self.magic_ability.cast_spell(getattr(self.spellbook, spell), target)
