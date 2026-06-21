from abc import ABC, abstractmethod

class AbstractCharacter(ABC):
    
    @abstractmethod
    def attack(self, target): pass
        
    @abstractmethod
    def take_damage(self, amount): pass

    @abstractmethod
    def special_move(self, target): pass
    
    @abstractmethod
    def heal(self): pass

    @abstractmethod
    def get_health(self): pass
    
    @abstractmethod
    def get_resource(self): pass