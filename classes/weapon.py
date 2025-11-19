

class Weapon:
    def __init__(self, typ:str, dmg:int):
        self._typ = typ
        self._dmg = dmg

    def __str__(self):
        return f"Your Weapon is {self._typ}, dealing {self._dmg} dmg"
        
