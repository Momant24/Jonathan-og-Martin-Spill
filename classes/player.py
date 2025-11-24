from .entity import Entity
from .weapon import Weapon
from random import randint


class Player(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: float, strength: float, typ: str, dmg: int ):
        Entity.__init__(self, name, hp, defence, strength)
        Weapon.__init__(self, typ, dmg)
        self._dmg = 0
        if typ == "Pinne":
            self._dmg = 2
        if typ == "Katana":
            self._dmg = 8
        elif typ == "Polearm":
            self._dmg = 10
        elif typ == "bow":
            self._dmg = 7
        
    def __str__(self):
        return Entity.__str__(self) + Weapon.__str__(self)
    
    
    def attack(self):
        critRate = randint(1,2)
        atk = self._dmg / self._strength
        critDmg = atk * critRate 
        print(f"You did {round(critDmg) * self._defence} damage to fiend")
        return round(critDmg)
    
    def dmg_taken(self):
        self._hp -= Player.attack(self) * self._defence 
        if self._hp > 0:
            print(f"you have {self._hp} hp remaining")
        elif self._hp < 0:
            self._hp = 0
            print("You have died")

    def dmg_verden(self, minusdm):
       self._hp = self._hp - minusdm

    def liv_igjenn(self):
        return(self._hp)
            
    
    
# spiller = Player("bob", 150, 1.5, 0.7, "Polearm", 45)
# print(spiller)
# Player.attack(spiller)
# Player.dmg_taken(spiller)


        
        
