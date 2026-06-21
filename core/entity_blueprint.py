from abc import ABC, abstractmethod

class AbstractCharacter(ABC):
    def __init__(self):
        self.statuses = {
            "stunned": False,
            "burn_turns": 0,
            "vulnerable": False,
            "dmg_reduction": False,
            "barrier": False,
            "parry": False,
            "attack_debuff": False
        }

    @abstractmethod
    def attack(self, target): pass
    @abstractmethod
    def special_move(self, target): pass
    @abstractmethod
    def heal(self): pass
    @abstractmethod
    def defend(self): pass
    @abstractmethod
    def utility(self, target): pass
    
    @abstractmethod
    def get_health(self): pass
    @abstractmethod
    def get_resource(self): pass
    @abstractmethod
    def roll_mood(self): pass
    @abstractmethod
    def full_heal(self): pass

    def process_statuses(self):
        msg = ""
        if self.statuses["burn_turns"] > 0:
            burn_dmg = 10
            self.take_damage(burn_dmg)
            self.statuses["burn_turns"] -= 1
            msg = f"🔥 {self.name} takes {burn_dmg} Burn damage! "
        
        self.statuses["dmg_reduction"] = False
        self.statuses["parry"] = False
        self.statuses["barrier"] = False
        return msg