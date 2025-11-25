from .entity import Entity
from .weapon import Weapon
from random import randint

class Enemy(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: float, strength: float, typ:str, dmg:int):
        Entity.__init__(self, name, hp, defence, strength)
        Weapon.__init__(self, typ, dmg)
        
    def __str__(self):
        return Entity.__str__(self) + Weapon.__str__(self)
    
    def attack(self,spiller):
        critRate = randint(1,2)
        atk = self._dmg / self._strength
        atk = atk / spiller._defence
        critDmg = round(atk)* critRate 
        print(f"{self._name} gjorde {round(critDmg)} skade på {spiller._name}")
        return round(critDmg)
    

