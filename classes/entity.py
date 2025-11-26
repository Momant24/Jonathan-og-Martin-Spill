class Entity:
    def __init__(self, name:str, hp:int, defence:float, strength:float):
        self._name = name
        self._maxHp = hp
        self._hp = self._maxHp
        self._defence = defence
        self._strength = strength
    
    def __str__(self):
        return f" Navn: {self._name} \n hp: {self._hp} \n forsvar: {self._defence} \n styrke: {self._strength} \n"
    

    
