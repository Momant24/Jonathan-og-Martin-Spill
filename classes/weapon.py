

class Weapon:
    def __init__(self, typ:str, dmg:int):
        self._typ = typ
        self._dmg = dmg
        self.set_damage()
        
    def set_damage(self):  
        typ = self._typ 
        if typ == "Skjor_Pinne":
            self._dmg = 1
        elif typ == "Pinne":
            self._dmg = 2
        elif typ == "Edel_Pinne":
            self._dmg = 5
        elif typ == "Reke_Sjell":
            self._dmg = 7
        elif typ == "Polearm":
            self._dmg = 10
        elif typ == "bow":
            self._dmg = 7

    def nyvopen(self, ny):
        self._typ = ny
        self.set_damage()

    def __str__(self):
        return f"\n Våpenet er {self._typ} \n {self._typ} gjør {self._dmg} skade"
        
