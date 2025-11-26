from .entity import Entity
from .weapon import Weapon
from random import randint
from .enemy import Enemy


class Player(Entity, Weapon):
    def __init__(self, name: str, hp: int, defence: float, strength: float, typ: str, dmg: int ):
        Entity.__init__(self, name, hp, defence, strength)
        Weapon.__init__(self, typ, dmg)
       
        
    def __str__(self):
        return Entity.__str__(self) + Weapon.__str__(self)

    
    def attack(self, fiende):
        critRate = randint(1,2)
        atk = self._dmg / self._strength
        atk = atk / fiende._defence
        critDmg = round(atk) * critRate 
        print(f"{self._name} gjorde {round(critDmg)} skade på {fiende._name}")
        return round(critDmg)
    
    def playerHeal(self): 
        potion = randint(1,3)
        helth = 0
        if potion == 1:
            helth = 20
        elif potion == 2:
            helth = 10
        elif potion == 3:
            helth = 5
        playerHelth = self._hp + helth
        print(f"du helbredet {helth} hp \n du har nå {self._hp} hp")
        return playerHelth
        
    

    def dmg_verden(self, minusdm):
       self._hp = self._hp - minusdm

    def liv_igjenn(self):
        return(self._hp)
            
spiller = Player("bob", 150, 1.5, 0.7, "Polearm", 45)


    
# print(spiller)
# Player.attack(spiller)
# Player.dmg_taken(spiller)


        
        
