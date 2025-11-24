class Entity:
    def __init__(self, name:str, hp:int, defence:float, strength:float):
        self._name = name
        self._hp = hp
        self._defence = defence
        self._strength = strength
    
    def __str__(self):
        return f"Entity, Name: {self._name} \n hp: {self._hp} \n defence: {self._defence} \n strength: {self._strength} \n"
    

    
