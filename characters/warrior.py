import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Warrior(AbstractCharacter):
    def __init__(self, name):
        self.name = name
        self.max_health = 150
        self.__health = self.max_health
        self.__rage = 0      
        self.__defense = 5
        self.attack_power = 20
        self.mood = "Normal"

    def get_health(self): return self.__health
    def get_resource(self): return self.__rage

    def full_heal(self):
        self.__health = self.max_health
        self.__rage = 0

    def roll_mood(self):
        roll = random.randint(1, 100)
        
        if self.__health < 40 and roll > 70:
            self.mood = "Berserk"
            return f"😡 BERSERK: {self.name} loses control! Defense drops, Attack surges!"
            
        elif self.__health < 20 and roll > 85:
            self.mood = "Last Stand"
            self.__health += 30
            return f"🛡️ LAST STAND: {self.name} refuses to fall! (+30 HP)"
            
        elif roll < 15:
            self.mood = "Adrenaline"
            self.__rage += 15
            if self.__rage > 100: self.__rage = 100
            return f"⚡ ADRENALINE: {self.name}'s blood pumps faster! (+15 Rage)"

        elif roll < 30:
            self.mood = "Focused"
            self.__health += 5
            if self.__health > self.max_health: self.__health = self.max_health
            return f"🧘 FOCUSED: {self.name} catches their breath. (+5 HP)"
            
        else:
            self.mood = "Normal"
            return random.choice([
                f"⚔️ {self.name} grips their weapon tightly.",
                f"👀 {self.name} circles the enemy.",
                f"💨 The battlefield is dead silent."
            ])

    def take_damage(self, amount):
        defense = 0 if self.mood == "Berserk" else self.__defense
        actual = max(amount - defense, 0)
        self.__health -= actual
        if self.__health < 0: self.__health = 0
        return f"🛡️ {self.name} takes {actual} damage!"

    def attack(self, target):
        self.__rage += 20
        if self.__rage > 100: self.__rage = 100
        damage = self.attack_power
        if self.mood == "Berserk": damage += 15
        if self.mood == "Last Stand": damage *= 2
        msg1 = f"🗡️ {self.name} swings a heavy broadsword!"
        msg2 = target.take_damage(damage)
        return f"{msg1}\n   {msg2}"

    def special_move(self, target):
        if self.__rage >= 50:
            self.__rage -= 50
            damage = self.attack_power * 2
            if self.mood == "Berserk": damage += 20
            msg1 = f"💥 {self.name} uses EXECUTE!"
            msg2 = target.take_damage(damage)
            return f"{msg1}\n   {msg2}"
        return f"❌ {self.name} lacks Rage (needs 50)!"

    def heal(self):
        self.__health += 30
        if self.__health > self.max_health: self.__health = self.max_health
        return f"🩹 {self.name} uses a bandage! Healed for 30."