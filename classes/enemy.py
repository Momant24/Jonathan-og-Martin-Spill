from .entity import Entity
from .weapon import Weapon
from random import randint

class Enemy(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: float, strength: float, typ:str, dmg:int):
        Entity.__init__(self, name, hp, defence, strength)
        Weapon.__init__(self, typ, dmg)
        
    def __str__(self):
        return f"{self._name}"
    
    def attack(self):
        critRate = randint(1,2)
        atk = self._dmg / self._strength
        critDmg = atk * critRate 
        print(f"You did {round(critDmg) * self._defence} damage to fiend")
        return round(critDmg)
    

