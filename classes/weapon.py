

class Weapon:
    def __init__(self, typ:str, dmg:int):
        typ = typ.capitalize()
        self._typ = typ
        self._dmg = dmg
        if typ == "Skjor_Pinne":
            self._dmg = 1
        elif typ == "Pinne":
            self._dmg = 2
        elif typ == "Edel_Pinne":
            self.dmg = 5
        elif typ == "Katana":
            self._dmg = 8
        elif typ == "Polearm":
            self._dmg = 10
        elif typ == "bow":
            self._dmg = 7

    def nyvopen(self, ny):
        self._typ = ny
    def __str__(self):
        return f"Your Weapon is {self._typ}, \n dealing {self._dmg} dmg"
        
