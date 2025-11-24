import time
import os
from random import randint
from classes import Player, Enemy

Fiskeånde = False

fiend = Enemy("Orc", 75, 1, 0.7, "pinne", 0)
def randomEncount():
    randEnc = randint(1,10)
    if randEnc >= 5:
        print(f"You have encountered an {fiend}")
    elif randEnc < 5:
        print(f"The {fiend} just about missed you")
    
def skog():
    valg = input("I skogen ser du et stort tre som er i full flamme ønsker du å risikere å bli angrepet ved å slukke treet(1), løpe vekk å gjemme deg(2), eller angripe på forhond?(3) ")
    os.system("cls")
    while valg != "1" and valg != "2" and valg != "3":
        valg = input("Feil velg enten 1 eller 2 eller 3: ")
    if valg == "1":
        print("Sekken din beynner å brenne å du mister 20 hp. Men du redder det gigantiske treet og han gir deg en edel pinne som gjør 5dm og sier at hvis du noen gang trenger hjelp vil han komme til din hjelp!")
        Karakteren.nyvopen("Edel_Pinne")
        print(f"Du her nå {Karakteren._typ} som våpen")
        nytt_sted()

    elif valg == "2":
        print("Du glmete baggen din i all hast og ser den bli tråkket på av treet. I den var pinnen din. Du finner en ny pinne på bakken men den ser tørr og skjør ut og vil bare ta 1 dm istede for di gamle 2")
        Karakteren.nyvopen("Skjor_Pinne")
        print(f"Du her nå {Karakteren._typ} som våpen")
        valg2 = input("Du gjemmer deg i en busk og kan velge å skjynte deg til sikkerhet(1), eller se om treet brenner opp å ta sakene deres.(2): ")
        os.system("cls")
        while valg2 != "1" and valg2 != "2":
            valg2 = input("Feil velg enten 1 eller 2: ")
        if valg2 == "2":
            print("Treet har brent opp til aske og du finner en Svidd_Edel_Pinne, men det detter en fugl i hodet ditt og du tar 20 dm")
            Karakteren.dmg_verden(20)
            Karakteren.nyvopen("Svidd_Edel_Pinne")
            print(f"Du her nå {Karakteren._typ} som våpen")
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")



        nytt_sted()
    
    else:
        print("Du kjemper")
        nytt_sted()
    
def nytt_sted():
    valg3 = input("Du ser en vakker insjø(1), og en stor glødene vulkan(2). Hvor vil du gå?: ")
    os.system("cls")
    while valg3 != "1" and valg3 != "2":
        valg4 = input("Feil velg enten 1 eller 2: ")

    if valg3 == "1":
        randomEncount()
        valg4 = input("Til venstre ser du insjøen dele seg i to som jesus står gjemt bak et tre og holder veien framover åpen for deg(1), eller ønsker du å ungå denne tråldommen og svømme over, du skimter små fisk i vannet(2): ")
        os.system("cls")
        while valg4 != "1" and valg3 != "2":
            valg4 = input("Feil velg enten 1 eller 2: ")
        if valg4 == "1":
            print("Du beveger deg usikker bortover den våte bunnen av insjøen med vannet stigende over deg på hvær sin side når en fisk flyr ut av den ene veggen rett inn i munnen din. Du føler deg god og mett og får 10 hp og en ånde stinkende av fisk")
            Karakteren.dmg_verden(-10)
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
            Fiskeånde = True
            andresiden()    
        else:
            valg5 = input("Du svømmer kjapt men skipter en fisk komme skytende mot deg den biter deg i rompa i det du kommer til land. Du tar 10 dm. Du kan velge ønsker du å stikke pirayaen på tuppen av en pinne og bruke den som våpen eller grille den?: ")
    else:
        
        print(f"Du falt ned til den den frydige skogen og tok 10 dm du har nå {Karakteren.liv_igjenn()} hp igjenn")
        os.system("cls")
        skog()

def andresiden():
    print("Yey nytt sted")



Start = input("Press s og så enter for å starte gamet: ")
os.system("cls")

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
    os.system("cls")
    while Førstelevvel != "1" and Førstelevvel != "2":
        Førstelevvel = input("Feil velg enten 1 eller 2: ")

    if Førstelevvel == "1":
        skog()
        
    else:
        Karakteren.dmg_verden(10)
        print(f"Du falt ned til den den frydige skogen og tok 10 dm du har nå {Karakteren.liv_igjenn()} hp igjenn")
        os.system("cls")
        skog()

        



   

