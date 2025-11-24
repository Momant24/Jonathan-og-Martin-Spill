import time
from random import randint
from classes import Player, Enemy

fiend = Enemy("Orc", 75, 1, 0.7, "pinne", 0)
def randomEncount():
    randEnc = randint(1,10)
    if randEnc >= 5:
        print(f"You have encountered an {fiend}")
    elif randEnc < 5:
        print(f"The {fiend} just about missed you")
    
def skog():
   valg = input("I skoge ser du et stort tre som er i full flamme ønsker du å risikere å bli angrepet å slukke treet(1), løpe vekk å gjemme deg(2), eller angripe på forhond?(3) ")
   while valg != "1" and Førstelevvel != "2":
        valg = input("Feil velg enten 1 eller 2 eller 3: ")        
        

Start = input("Press s og så enter for å starte gamet: ")

if Start == "S" or Start == "s":
    print("Starter spill")
    for i in range(0):
        print("*", end="\r")
        time.sleep(0.5)
        print(" *", end="\r")
        time.sleep(0.5)
        print("  *", end="\r") 
        time.sleep(0.5)
        print("   *", end="\r") 
        time.sleep(0.5)
        print("    ", end="\r")
    Navn = input("Hva skal karakteren din hete?: ")
    Karakteren = Player(Navn, 100, 1, 0.7, "Pinne", 0)
    print(Karakteren)

    
    Førstelevvel = input("Du har 2 valg ønsker du å gå inn i en frydig skog(1) eller gå til en Flyvende øy(2): ")

    while Førstelevvel != "1" and Førstelevvel != "2":
        Førstelevvel = input("Feil velg enten 1 eller 2: ")

    if Førstelevvel == 1:
        skog()
    else:
        Karakteren.dmg_verden(10)
        print(f"Du falt ned til den den frydige skogen og tok 10 dm du har nå {Karakteren.liv_igjenn()} hp igjenn")

        



   

