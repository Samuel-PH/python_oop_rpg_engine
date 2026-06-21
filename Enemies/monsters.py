import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter
from characters.warrior import Warrior
from characters.mage import Mage

class Goblin(AbstractCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Sneaky Goblin"
        self.__health = 40
        self.__energy = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__energy
    def full_heal(self): pass
    def roll_mood(self): return "🐀 The Goblin chatters nervously."
    def take_damage(self, amount):
        actual = amount + 10 if self.statuses["vulnerable"] else amount
        self.__health = max(self.__health - actual, 0)
        return actual, "HIT"
    def attack(self, target): 
        dmg, _ = target.take_damage(10)
        return f"🔪 Goblin stabs for {dmg} damage!"
    def special_move(self, target): return self.attack(target)
    def heal(self): return "❌ Goblins can't heal!"
    def defend(self): return "💨 Goblin tries to hide."
    def utility(self, target): return "💬 Goblin spits at you."

class Orc(AbstractCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Brutal Orc"
        self.__health = 90
        self.__stamina = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__stamina
    def full_heal(self): pass
    def roll_mood(self): return "👹 The Orc beats its chest!"
    def take_damage(self, amount):
        actual = amount // 2 if self.statuses["dmg_reduction"] else amount
        actual = actual + 10 if self.statuses["vulnerable"] else actual
        self.__health = max(self.__health - actual, 0)
        return actual, "HIT"
    def attack(self, target): 
        dmg, _ = target.take_damage(15)
        return f"🪓 Orc swings an axe for {dmg} damage!"
    def special_move(self, target): return self.attack(target)
    def heal(self): return "❌ Orcs prefer pain!"
    def defend(self): 
        self.statuses["dmg_reduction"] = True
        return "🛡️ Orc braces for impact! (Damage halved)"
    def utility(self, target): return "👹 Orc roars loudly!"

class DarkElf(AbstractCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Corrupted Elf"
        self.__health = 100
        self.__mana = 100 
    def get_health(self): return self.__health
    def get_resource(self): return self.__mana
    def full_heal(self): pass
    def roll_mood(self): return "🧝 The Elf whispers a dark curse."
    def take_damage(self, amount):
        if self.statuses["barrier"]:
            self.statuses["barrier"] = False
            return 0, "BARRIER"
        actual = amount + 10 if self.statuses["vulnerable"] else amount
        self.__health = max(self.__health - actual, 0)
        return actual, "HIT"
    def attack(self, target): 
        dmg, _ = target.take_damage(12)
        return f"🏹 Elf fires a shadow arrow for {dmg} damage!"
    def special_move(self, target): return self.attack(target)
    def heal(self): 
        self.__health = min(self.__health + 20, 100)
        return "🩸 Elf leeches life! (+20 HP)"
    def defend(self):
        self.statuses["barrier"] = True
        return "🛡️ Elf conjures a dark barrier! (Deflects next hit)"
    def utility(self, target): return "🌑 Elf blends into the shadows."

class DemonLord(AbstractCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Azazel, Demon Lord"
        self.__health = 300
        self.__dark_magic = 100 
        self.mood = "Normal"
    def get_health(self): return self.__health
    def get_resource(self): return self.__dark_magic
    def full_heal(self): pass

    def roll_mood(self):
        roll = random.randint(1, 100)
        if roll > 80:
            self.mood = "Arrogant"
            self.statuses["vulnerable"] = True
            return "👿 Azazel laughs arrogantly! He leaves his guard open! (Vulnerable)"
        elif roll < 20:
            self.mood = "Enraged"
            return "🔥 Azazel's eyes glow with hellfire! (Damage Increased)"
        self.mood = "Normal"
        return "👿 Azazel glares at you."

    def take_damage(self, amount):
        if self.statuses["barrier"]:
            self.statuses["barrier"] = False
            return 0, "BARRIER"
        actual = amount + 15 if self.statuses["vulnerable"] else amount
        self.__health = max(self.__health - actual, 0)
        return actual, "HIT"

    def attack(self, target):
        base_dmg = 15 if self.mood == "Arrogant" else 25
        base_dmg = 40 if self.mood == "Enraged" else base_dmg
        dmg, _ = target.take_damage(base_dmg)
        return f"⚔️ Azazel strikes with a flaming whip for {dmg} damage!"

    def special_move(self, target):
        if self.__dark_magic >= 40:
            self.__dark_magic -= 40
            target.statuses["attack_debuff"] = True
            return f"🌑 SOUL CRUSH! {target.name}'s attack power is weakened next turn!"
        return self.attack(target)

    def heal(self): 
        self.__health = min(self.__health + 30, 300)
        return "🩸 Azazel drains shadows! (+30 HP)"

    def defend(self):
        self.statuses["barrier"] = True
        return "🛡️ Azazel wraps himself in Demonic Wings! (Deflects next hit)"
        
    def utility(self, target): return "🔥 Azazel summons hellfire."