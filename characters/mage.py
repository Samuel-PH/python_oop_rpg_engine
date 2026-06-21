import sys, os, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.entity_blueprint import AbstractCharacter

class Mage(AbstractCharacter):
    def __init__(self, name):
        self.name = name
        self.__health = 80   
        self.__mana = 100    
        self.attack_power = 15
        self.mood = "Normal" 

    def get_health(self): return self.__health
    def get_resource(self): return self.__mana

    def roll_mood(self):
        roll = random.randint(1, 100)
        
        if self.__health > 0 and self.__health < 15 and roll > 80:
            self.mood = "Last Stand"
            self.__health += 20 
            return f"🌟 TIME OF NEED: {self.name} is filled with sudden determination! (+20 HP)"

        elif self.__health < 30 and roll < 40:
            self.mood = "Panic"
            return f"😨 PANIC: {self.name} is trembling. Her focus is breaking!"
            
        elif roll > 85:
            self.mood = "Inspired"
            return f"✨ INSPIRED: Arcane energy swirls perfectly around {self.name}!"
            
        else:
            self.mood = "Normal"
            flavors = [
                f"💨 The wind howls across the battlefield...",
                f"👀 {self.name} analyzes the enemy's stance.",
                f"⚡ Static electricity crackles in the air."
            ]
            return random.choice(flavors)

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0: self.__health = 0
        return f"🧙 {self.name}'s barrier takes {amount} damage!"

    def attack(self, target):
        if self.mood == "Panic" and random.randint(1, 100) < 50:
            return f"❌ {self.name} fumbles the incantation! The spell fizzles out!"

        damage = self.attack_power
        if self.mood == "Inspired": damage += 10
        if self.mood == "Last Stand": damage *= 2

        self.__mana += 10 
        if self.__mana > 100: self.__mana = 100
        
        msg1 = f"✨ {self.name} fires a magic missile!"
        msg2 = target.take_damage(damage)
        return f"{msg1}\n   {msg2}"

    def special_move(self, target):
        if self.mood == "Panic" and random.randint(1, 100) < 30:
            return f"❌ {self.name} panics and drops the fireball!"
            
        mana_cost = 0 if self.mood == "Inspired" else 40

        if self.__mana >= mana_cost:
            self.__mana -= mana_cost
            damage = 40 if self.mood == "Last Stand" else 30
            msg1 = f"🔥 {self.name} casts PYROBLAST!"
            msg2 = target.take_damage(damage)
            return f"{msg1}\n   {msg2}"
        else:
            return f"❌ {self.name} is out of Mana!"

    def heal(self):
        if self.__mana >= 30:
            self.__mana -= 30
            self.__health += 40
            if self.__health > 80: self.__health = 80
            return f"💚 {self.name} casts Healing Spell! Restored 40 HP."
        return f"❌ {self.name} lacks Mana to heal!"