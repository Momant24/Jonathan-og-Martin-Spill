from .entity import Entity
from .weapon import Weapon
from random import randint



class Player(Entity, Weapon):

    def __init__(self, name: str, hp: int, defence: float, strength: float, typ: str, dmg: int ):
        Entity.__init__(self, name, hp, defence, strength)
        Weapon.__init__(self, typ, dmg)
        self._fiske_onde = 0
        
    def __str__(self):
        return Entity.__str__(self) + Weapon.__str__(self)

    def plusdefence(self, ekstradf):
        self._defence = self._defence + ekstradf
        return f"Du har nå {self._defence} i defence"
    
      #arrack funksjon som kalles i enemydmg taken funksjonen i game.py
    def attack(self, fiende):
        critRate = randint(1,2)
        atk = self._dmg / self._strength
        atk = atk / fiende._defence
        critDmg = round(atk) * critRate 
        print(f"\n{self._name} gjorde {round(critDmg)} skade på {fiende._name}")
        return round(critDmg)
    
    #healer spiller funkjsonen
    def playerHeal(self): 
        potion = randint(1,3)
        helth = 0
        if potion == 1:
            helth = 20
        elif potion == 2:
            helth = 10
        elif potion == 3:
            helth = 5
        self._hp = self._hp + helth
        if self._hp > self._maxHp:
            self._hp = self._maxHp
        print(f"\n du helbredet {helth} hp \n du har nå {self._hp} hp \n\n")

        
    

    def dmg_verden(self, minusdm):
       self._hp = self._hp - minusdm
       if self._hp > self._maxHp:  #Dette er meningen
           self._maxHp = self._hp
    
    def fultliv(self):
        self._hp = self._maxHp

    def liv_igjenn(self):
        return(self._hp)


        
        
