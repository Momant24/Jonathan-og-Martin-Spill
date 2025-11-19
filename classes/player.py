from entity import Entity
from weapon import Weapon
from random import randint

class Player(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: int, strength: int, typ: str, dmg: int ):
        Entity.__init__(self, name, hp, defence, strength)
        self._hp = 500
        self._defence = 20
        self._strength = 0.5
        Weapon.__init__(self, typ, dmg)
        self._dmg = 0
        if typ == "Katana":
            self._dmg = 38
        elif typ == "Polearm":
            self._dmg = 40
        elif typ == "bow":
            self._dmg = 28
        
    def __str__(self):
        return Entity.__str__(self) + Weapon.__str__(self)
    
    
    def attack(self):
        critRate = randint(1,2)
        atk = self._dmg / self._strength
        critDmg = atk * critRate
        print()
        return critDmg
    
    def dmg_taken(self):
        self._hp -= Player.attack(self)
        if self._hp > 0:
            print(f"you have {self._hp} hp remaining")
        elif self._hp < 0:
            self._hp = 0
            print("You have died")
    
    
spiller = Player("bob", 150, 20, 50, "Polearm", 45)
print(spiller)
Player.attack(spiller)
Player.dmg_taken(spiller)