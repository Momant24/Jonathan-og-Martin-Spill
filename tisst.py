from classes import Player, Enemy
from game import Karakteren, fiend
from random import randint
import time

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
    print(" Du er blitt angrepet!")
    time.sleep(0.5)
    print(f" Din fiende er en {fiende._name}")
    print(fiend)

    
    while karakter._hp > 0 and fiende._hp > 0:   
        #valg av handlinger
        time.sleep(1)
        print("\n Dine valg!")
        print(" 1: angrip \n 2: helbred deg selv \n 3: Ryggsekk")

        # spiller sin tur
        time.sleep(0.5)
        a = input("Hva velger du å gjøre?")
        if a == "1":
            EnmyDmg_taken(fiende, karakter)
            
        elif a == "2":
            karakter.playerHeal()
        elif a == "3":
            print(" dust du har ikke en ryggsekk ennå")
        else:
            print(" Ugyldig valg, prøv igjen: \n\n Dine valg! \n 1: angrip \n 2: Helbred degselb \n 3: ryggsekk")
            a = input("Velg på nytt:")
        time.sleep(1)

        # stoppe loop hvis fienden er død
        if fiende._hp <= 0:
            break
        
        #Fiende sin tur
        chance = randint(1,20)
        if chance > 15:
            fiende.enemyrHeal()
        else:
            print(f"\n {fiende._name} Angriper")
            PlayerDmg_taken(karakter, fiende)
        
        #stoppe loop hvis spiller er død
        if karakter._hp <= 0:
            break
        # hivs du vinner combat
    if karakter._hp <= 0:  
        print(f"{karakter._name} døde, hva er det du gjør?")
        return kjemper(karakter, fiende)
    elif fiende._hp <= 0:       
         print(f"{fiende._name} er død, du vant!")   
        
def retryFight(karakter, fiende):
    while True:
        kjemper(karakter, fiende)
        
        if karakter._hp > 0:
            print(" Du overlevde")
            
kjemper(Karakteren, fiend)
        
        
    