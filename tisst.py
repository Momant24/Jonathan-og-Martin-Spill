from classes import Player, Enemy
from game import Karakteren, fiend

def EnmyDmg_taken(fiende, karakter):
    fiende._hp -= Player.attack(karakter) * karakter._defence 
    if karakter._hp > 0:
        print(f"{fiende} have {fiende._hp} hp remaining")
    elif fiende._hp < 0:
        fiende._hp = 0
        print(f"{fiende} have died")
        
def PlayerDmg_taken(karakter, fiende):
    karakter._hp -= Enemy.attack(fiende) * fiende._defence 
    if karakter._hp > 0:
        print(f"{karakter._name} have {karakter._hp} hp remaining")
    elif karakter._hp < 0:
        karakter._hp = 0
        print(f"{karakter._name} have died")

def kjemper(karakter, fiende):
    playerTurn = True
    print("Du er blitt angrepet \n 1 for å angripe!")
    while karakter._hp or fiende._hp < 0:
        while playerTurn == True:
            a = input("")
            if a == "1":
                EnmyDmg_taken(fiend, Karakteren)
                return playerTurn == False
            
        while playerTurn == False:
            PlayerDmg_taken(Karakteren, fiend)
                
                       
            
        
            
kjemper(Karakteren, fiend)
        
        
    