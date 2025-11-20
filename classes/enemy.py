from .entity import Entity
from .weapon import Weapon

class Enemy(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: float, strength: float, typ:str, dmg:int):
        Entity.__init__(self, name, hp, defence, strength)
        Weapon.__init__(self, typ, dmg)
        
    def __str__(self):
        return f"{self._name}"