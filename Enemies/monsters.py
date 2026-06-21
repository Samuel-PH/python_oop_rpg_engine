import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Goblin(AbstractCharacter):
    def __init__(self):
        self.name = "Sneaky Goblin"
        self.__health = 40
        self.__energy = 100 
        self.mood = "Normal"

    def get_health(self): return self.__health
    def get_resource(self): return self.__energy

    def roll_mood(self):
        roll = random.randint(1, 100)
        if roll > 80:
            self.mood = "Cowardly"
            return f"🐀 {self.name} looks like it wants to run away!"
        self.mood = "Normal"
        return f"💬 {self.name} chatters its teeth menacingly."

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0: self.__health = 0
        return f"👺 {self.name} squeals, taking {amount} damage!"

    def attack(self, target):
        if self.mood == "Cowardly":
            return f"💨 {self.name} is too scared to attack this turn!"
        msg1 = f"🔪 {self.name} stabs with a rusty dagger!"
        msg2 = target.take_damage(10)
        return f"{msg1}\n   {msg2}"

    def special_move(self, target):
        return self.attack(target) 

    def heal(self):
        return f"❌ Goblins don't know how to heal!"

class DemonLord(AbstractCharacter):
    def __init__(self):
        self.name = "Azazel, The Demon Lord"
        self.__health = 250
        self.__dark_magic = 100 
        self.mood = "Arrogant"

    def get_health(self): return self.__health
    def get_resource(self): return self.__dark_magic

    def roll_mood(self):
        if self.__health < 100:
            self.mood = "Enraged"
            return f"🔥 AZAZEL IS ENRAGED! The room fills with hellfire!"
        return f"👿 Azazel laughs at your pathetic attempts."

    def take_damage(self, amount):
        actual = max(amount - 5, 0)
        self.__health -= actual
        if self.__health < 0: self.__health = 0
        return f"👿 Azazel shrugs off the blow, taking {actual} damage."

    def attack(self, target):
        damage = 25 if self.mood == "Enraged" else 15
        msg1 = f"⚔️ Azazel swings a massive flaming whip!"
        msg2 = target.take_damage(damage)
        return f"{msg1}\n   {msg2}"

    def special_move(self, target):
        if self.__dark_magic >= 50:
            self.__dark_magic -= 50
            msg1 = f"🌑 Azazel casts SOUL CRUSH!"
            msg2 = target.take_damage(40)
            return f"{msg1}\n   {msg2}"
        return self.attack(target)

    def heal(self):
        self.__health += 20
        if self.__health > 250: self.__health = 250
        return f"🩸 Azazel drains life from the shadows! (+20 HP)"