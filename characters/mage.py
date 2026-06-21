import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Mage(AbstractCharacter):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.max_health = 80
        self.__health = self.max_health   
        self.__mana = 100    
        self.attack_power = 15
        self.mood = "Normal" 

    def get_health(self): return self.__health
    def get_resource(self): return self.__mana
    def full_heal(self): 
        self.__health = self.max_health
        self.__mana = 100
        for k in self.statuses: self.statuses[k] = False

    def roll_mood(self):
        roll = random.randint(1, 100)
        if self.__health < 20 and roll > 80:
            self.mood = "Last Stand"
            self.__health += 30 
            for k in self.statuses: self.statuses[k] = False
            return f"🌟 TIME OF NEED: {self.name} clears all debuffs and heals! (+30 HP)"
        elif roll < 20:
            self.mood = "Mana Surge"
            self.__mana = min(self.__mana + 20, 100)
            return f"🔵 SURGE: Leylines pulse beneath {self.name}! (+20 Mana)"
        self.mood = "Normal"
        return f"✨ Arcane energy hums around {self.name}."

    def take_damage(self, amount):
        if self.statuses["barrier"]:
            self.statuses["barrier"] = False
            self.__mana = min(self.__mana + 20, 100)
            return 0, "BARRIER"
            
        actual = amount
        if self.statuses["dmg_reduction"]: actual //= 2
        if self.statuses["vulnerable"]: actual += 10

        self.__health = max(self.__health - actual, 0)
        return actual, "HIT"

    def attack(self, target):
        element = random.choice(["Fire", "Thunder", "Water"])
        dmg, effect = target.take_damage(self.attack_power)
        
        if effect in ["PARRY", "BARRIER"]: return f"💥 The spell was deflected by {target.name}!"
        
        if element == "Fire":
            target.statuses["burn_turns"] = 2
            return f"🔥 FIREBALL! {target.name} takes {dmg} dmg and is IGNITED!"
        elif element == "Thunder":
            if random.randint(1, 100) > 60:
                target.statuses["stunned"] = True
                return f"⚡ CHAIN LIGHTNING! {target.name} takes {dmg} dmg and is STUNNED!"
            return f"⚡ LIGHTNING BOLT! {target.name} takes {dmg} dmg."
        else: # Water
            self.__health = min(self.__health + 10, self.max_health)
            self.__mana = min(self.__mana + 15, 100)
            return f"🌊 WATER BLAST! {target.name} takes {dmg} dmg. {self.name} siphons HP & Mana!"

    def special_move(self, target):
        if self.__mana >= 40:
            self.__mana -= 40
            dmg, effect = target.take_damage(40)
            if effect in ["PARRY", "BARRIER"]: return f"💥 PYROBLAST was deflected!"
            return f"🌋 PYROBLAST! {target.name} takes {dmg} massive damage!"
        return f"❌ Out of Mana!"

    def heal(self):
        if self.__mana >= 30:
            self.__mana -= 30
            self.__health = min(self.__health + 40, self.max_health)
            return f"💚 Healing Spell! Restored 40 HP."
        return f"❌ Lacks Mana to heal!"

    def defend(self):
        if random.randint(1, 100) > 50:
            self.statuses["barrier"] = True
            return f"🛡️ {self.name} conjures an Arcane Barrier! Deflects next attack & restores Mana!"
        self.statuses["dmg_reduction"] = True
        return f"🛡️ {self.name} casts Shield. Incoming damage halved!"

    def utility(self, target):
        self.__mana = min(self.__mana + 40, 100)
        self.statuses["dmg_reduction"] = True
        return f"🧘 CHANNEL MANA: {self.name} focuses deeply. (+40 Mana, Damage Halved next turn)"