from classes import Player, Enemy
from game import Karakteren, fiend

#funksjon for skade av orc
def EnmyDmg_taken(fiende, karakter):
    fiende._hp -= Player.attack(karakter, fiende)
    if karakter._hp > 0:
        print(f"{fiende._name} har {fiende._hp} hp igjen")
    elif fiende._hp < 0:
        fiende._hp = 0

        #funksjon for skade på spiller
def PlayerDmg_taken(karakter, fiende):
    karakter._hp -= Enemy.attack(fiende, karakter)
    if karakter._hp > 0:
        print(f"{karakter._name} har {karakter._hp} hp igjen")
    elif karakter._hp < 0:
        karakter._hp = 0



#fuknsjon for combat
def kjemper(karakter, fiende):
    print(fiend)
    print("Du er blitt angrepet!")
    
    while karakter._hp > 0 or fiende._hp > 0:   
        #valg av handlinger
        print("\n Dine valg!")
        print("1: angrip")
        print("2: helbred deg selv")
        print("3: Ryggsekk")

        # spiller sin tur
        a = input("Hva velger du å gjøre?")
        if a == "1":
            EnmyDmg_taken(fiende, karakter)
        else:
            print("ugyldig valg, prøv igjen:")
            print("\n Dine valg!")
            print("1: angrip")
            print("2: helbred deg selv")
            print("3: Ryggsekk")
            a = input("Velg på nytt:")


        # stoppe loop hvis fienden er død
        if fiende._hp <= 0:
            break
        
        #Fiende sin tur
        print(f"\n {fiende._name} Angriper")
        PlayerDmg_taken(karakter, fiende)
        
        #stoppe loop hvis spiller er død
        if karakter._hp <= 0:
            break
        # hivs du vinner combat
    if karakter._hp <= 0:  
        print(f"{karakter._name} døde, hva er det du gjør?")
    elif fiende._hp <= 0:       
         print(f"{fiende._name} er død, du vant!")   
        
            
kjemper(Karakteren, fiend)
        
        
    