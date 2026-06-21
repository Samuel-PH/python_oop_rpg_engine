import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Goblin(AbstractCharacter):
    def __init__(self):
        self.name = "Sneaky Goblin"
        self.__health = 40
        self.__energy = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__energy
    def full_heal(self): pass
    def roll_mood(self): return "🐀 The Goblin chatters nervously."
    def take_damage(self, amount):
        self.__health = max(self.__health - amount, 0)
        return f"👺 Goblin squeals, taking {amount} damage!"
    def attack(self, target): return f"🔪 Goblin stabs!\n   {target.take_damage(10)}"
    def special_move(self, target): return self.attack(target)
    def heal(self): return "❌ Goblins can't heal!"

class Orc(AbstractCharacter):
    def __init__(self):
        self.name = "Brutal Orc"
        self.__health = 80
        self.__stamina = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__stamina
    def full_heal(self): pass
    def roll_mood(self): return "👹 The Orc beats its chest!"
    def take_damage(self, amount):
        self.__health = max(self.__health - amount, 0)
        return f"👹 Orc grunts, taking {amount} damage!"
    def attack(self, target): return f"🪓 Orc swings an axe!\n   {target.take_damage(15)}"
    def special_move(self, target): return f"🔨 Orc SMASH!\n   {target.take_damage(25)}"
    def heal(self): return "❌ Orcs prefer pain!"

class DarkElf(AbstractCharacter):
    def __init__(self):
        self.name = "Corrupted Elf"
        self.__health = 100
        self.__mana = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__mana
    def full_heal(self): pass
    def roll_mood(self): return "🧝 The Elf whispers a dark curse."
    def take_damage(self, amount):
        self.__health = max(self.__health - amount, 0)
        return f"🧝 Elf hisses, taking {amount} damage!"
    def attack(self, target): return f"🏹 Elf fires a shadow arrow!\n   {target.take_damage(12)}"
    def special_move(self, target): return f"🌑 Elf casts VOID BOLT!\n   {target.take_damage(30)}"
    def heal(self): 
        self.__health = min(self.__health + 20, 100)
        return "🩸 Elf leeches life from the earth! (+20 HP)"

class DemonLord(AbstractCharacter):
    def __init__(self):
        self.name = "Azazel, Demon Lord"
        self.__health = 250
        self.__dark_magic = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__dark_magic
    def full_heal(self): pass
    def roll_mood(self): return "👿 Azazel laughs at your pathetic attempts."
    def take_damage(self, amount):
        self.__health = max(self.__health - (amount - 5), 0)
        return f"👿 Azazel shrugs off the blow, taking {amount - 5} damage."
    def attack(self, target): return f"⚔️ Azazel swings a flaming whip!\n   {target.take_damage(20)}"
    def special_move(self, target): return f"🌑 Azazel casts SOUL CRUSH!\n   {target.take_damage(40)}"
    def heal(self): 
        self.__health = min(self.__health + 20, 250)
        return "🩸 Azazel drains shadows! (+20 HP)"