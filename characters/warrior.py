import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Warrior(AbstractCharacter):
    def __init__(self, name):
        self.name = name
        self.__health = 150
        self.__rage = 0
        self.__defense = 5
        self.attack_power = 20

    def get_health(self): return self.__health
    def get_resource(self): return self.__rage

    def take_damage(self, amount):
        actual_damage = max(amount - self.__defense, 0)
        self.__health -= actual_damage
        if self.__health < 0: self.__health = 0
        return f"🛡️ {self.name} blocks, taking {actual_damage} damage!"

    def attack(self, target):
        self.__rage += 20
        if self.__rage > 100: self.__rage = 100
        msg1 = f"🗡️ {self.name} swings a heavy broadsword!"
        msg2 = target.take_damage(self.attack_power)
        return f"{msg1}\n   {msg2}"

    def special_move(self, target):
        if self.__rage >= 50:
            self.__rage -= 50
            msg1 = f"💥 {self.name} uses EXECUTE! Massive damage!"
            msg2 = target.take_damage(self.attack_power * 2)
            return f"{msg1}\n   {msg2}"
        else:
            return f"❌ {self.name} doesn't have enough Rage (needs 50)!"

    def heal(self):
        heal_amt = 30
        self.__health += heal_amt
        if self.__health > 150: self.__health = 150
        return f"🩹 {self.name} uses a bandage! Healed for {heal_amt}."