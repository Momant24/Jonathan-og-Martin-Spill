class Entity:
    def __init__(self, name:str, hp:int, defence:int, strength:int):
        self._name = name
        self._hp = hp
        self._defence = defence
        self._strength = strength
    
    def __str__(self):
        return f"Entity, Name: {self._name}, hp: {self._hp} , defence: {self._defence} , strength: {self._strength} , "
    

    
