import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Warrior(AbstractCharacter):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.max_health = 150
        self.__health = self.max_health
        self.__rage = 0      
        self.attack_power = 20
        self.mood = "Normal"

    def get_health(self): return self.__health
    def get_resource(self): return self.__rage
    def full_heal(self): 
        self.__health = self.max_health
        self.__rage = 0
        for k in self.statuses: self.statuses[k] = False

    def roll_mood(self):
        roll = random.randint(1, 100)
        if self.__health < 30 and roll > 80:
            self.mood = "Last Stand"
            self.__health += 40
            for k in self.statuses: self.statuses[k] = False # Cleanses debuffs!
            return f"🛡️ LAST STAND: {self.name} is filled with determination! Debuffs cleansed! (+40 HP)"
        elif roll < 15:
            self.mood = "Adrenaline"
            self.__rage = min(self.__rage + 20, 100)
            return f"⚡ ADRENALINE: {self.name}'s blood pumps faster! (+20 Rage)"
        else:
            self.mood = "Normal"
            return f"⚔️ {self.name} grips their weapon tightly."

    def take_damage(self, amount):
        if self.statuses["parry"]:
            self.statuses["parry"] = False
            return 0, "PARRY" # Triggers stun on attacker in GUI
            
        actual = amount
        if self.statuses["dmg_reduction"]: actual //= 2
        if self.statuses["vulnerable"]: actual += 10
        if self.statuses["attack_debuff"]: actual = max(actual - 10, 0)

        self.__health = max(self.__health - actual, 0)
        return actual, "HIT"

    def attack(self, target):
        self.__rage = min(self.__rage + 20, 100)
        dmg, effect = target.take_damage(self.attack_power)
        if effect == "PARRY":
            self.statuses["stunned"] = True
            return f"💥 {target.name} PARRIED the attack! {self.name} is Stunned!"
        elif effect == "BARRIER":
            return f"✨ {target.name}'s Barrier absorbed the attack!"
        return f"🗡️ {self.name} swings a heavy broadsword! {target.name} takes {dmg} dmg!"

    def special_move(self, target):
        if self.__rage >= 50:
            self.__rage -= 50
            dmg, effect = target.take_damage(self.attack_power * 2)
            if effect in ["PARRY", "BARRIER"]: return f"💥 EXECUTE was deflected by {target.name}!"
            return f"💥 {self.name} uses EXECUTE! {target.name} takes {dmg} dmg!"
        return f"❌ Not enough Rage (needs 50)!"

    def heal(self):
        self.__health = min(self.__health + 30, self.max_health)
        return f"🩹 {self.name} uses a bandage! Healed for 30 HP."

    def defend(self):
        if random.randint(1, 100) > 70:
            self.statuses["parry"] = True
            return f"🛡️ {self.name} enters a PARRY stance! Next attack will be deflected!"
        self.statuses["dmg_reduction"] = True
        return f"🛡️ {self.name} raises their guard. Incoming damage halved!"

    def utility(self, target):
        self.__rage = min(self.__rage + 30, 100)
        roll = random.randint(1, 100)
        if roll > 60:
            target.statuses["vulnerable"] = True
            return f"🗣️ WARCRY! {self.name} gains Rage! {target.name} is intimidated and Vulnerable!"
        return f"🗣️ WARCRY! {self.name} gains 30 Rage, but {target.name} is unfazed."