import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Mage(AbstractCharacter):
    def __init__(self, name):
        self.name = name
        self.__health = 80
        self.__mana = 100 
        self.attack_power = 10

    def get_health(self): return self.__health
    def get_resource(self): return self.__mana

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0: self.__health = 0
        return f"🧙 {self.name}'s barrier shatters! Took {amount} damage!"

    def attack(self, target):
        self.__mana += 10
        if self.__mana > 100: self.__mana = 100
        msg1 = f"✨ {self.name} fires a magic wand!"
        msg2 = target.take_damage(self.attack_power)
        return f"{msg1}\n   {msg2}"

    def special_move(self, target):
        if self.__mana >= 40:
            self.__mana -= 40
            msg1 = f"🔥 {self.name} casts PYROBLAST! It ignores defense!"
            msg2 = target.take_damage(35) 
            return f"{msg1}\n   {msg2}"
        else:
            return f"❌ {self.name} is out of Mana!"

    def heal(self):
        if self.__mana >= 30:
            self.__mana -= 30
            self.__health += 40
            if self.__health > 80: self.__health = 80
            return f"💚 {self.name} casts Healing Spell! Restored 40 HP."
        else:
            return f"❌ {self.name} lacks Mana to heal!"