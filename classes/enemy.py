from .entity import Entity
from .weapon import Weapon

class Enemy(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: int, strength: float):
        Entity.__init__(self, name, hp, defence, strength)