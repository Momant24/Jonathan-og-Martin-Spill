import time
import os
from random import randint
from classes import Player, Enemy

Fiskeånde = 0
venner = []
uvenner = []

fiend = Enemy("Orc", 75, 1, 0.7, "pinne", 0)
def randomEncount():
    randEnc = randint(1,10)
    if randEnc >= 5:
        print(f"You have encountered an {fiend}")
    elif randEnc < 5:
        print(f"The {fiend} just about missed you")
    
def skog():
    global venner
    valg = input("I skogen ser du et stort tre som er i full flamme ønsker du å risikere å bli angrepet ved å slukke treet(1), løpe vekk å gjemme deg(2), eller angripe på forhond?(3) ")
    os.system("cls")
    while valg != "1" and valg != "2" and valg != "3":
        valg = input("Feil velg enten 1 eller 2 eller 3: ")
    if valg == "1":
        print("Sekken din beynner å brenne å du mister 20 hp. Men du redder det gigantiske treet og han gir deg en edel pinne som gjør 5dm og sier at hvis du noen gang trenger hjelp vil han komme til din hjelp!")
        Karakteren.nyvopen("Edel_Pinne")
        print(f"Du her nå {Karakteren._typ} som våpen")
        venner.append("Storttree")
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
    global Fiskeånde
    global venner
    global uvenner

    valg3 = input("Du ser en vakker insjø(1), og en stor glødene vulkan(2). Hvor vil du gå?: ")
    os.system("cls")
    while valg3 != "1" and valg3 != "2":
        valg4 = input("Feil velg enten 1 eller 2: ")

    if valg3 == "1":
        randomEncount()
        valg4 = input("Til venstre ser du insjøen dele seg i to som jesus står gjemt bak et tre og holder veien framover åpen for deg(1), eller ønsker du å ungå denne tråldommen og svømme over, du skimter små fisk i vannet(2): ")
        os.system("cls")
        while valg4 != "1" and valg4 != "2":
            valg4 = input("Feil velg enten 1 eller 2: ")
        if valg4 == "1":
            print("Du beveger deg usikker bortover den våte bunnen av insjøen med vannet stigende over deg på hvær sin side når en fisk flyr ut av den ene veggen rett inn i munnen din. Du føler deg god og mett og får 10 hp og en ånde stinkende av fisk")
            Karakteren.dmg_verden(-10)
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
            
            Fiskeånde += 1
           
        else:
            valg5 = input("Du svømmer kjapt men skipter en fisk komme skytende mot deg den biter deg i rompa i det du kommer til land. Du tar 10 dm. Du kan velge ønsker du å stikke pirayaen på tuppen av en pinne og bruke den som våpen(1), eller grille den?(2): ")
            os.system("cls")
            Karakteren.dmg_verden(10)
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")

            while valg5 != "1" and valg5 != "2":
                valg5 = input("Feil velg enten 1 eller 2: ")
            if valg5 == "1":
                Karakteren.nyvopen("Piraya_Pinne")
                print(f"Du her nå {Karakteren._typ} som våpen og {Karakteren._dmg} dmg")
            else:
                Karakteren.dmg_verden(-25)
                print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
        valg6 = input("Du ser en stor rullende reke som ruller rundt i en sirkel. Den er minst 7 ganger så stor som deg. Vil du gå og rulle med reken(1), vil du gå å ta en bit av reken(2), eller ønsker du og angripe reken(3).")
        os.system("cls")
        while valg6 != "1" and valg6 != "2" and valg6 != "3":
            valg6 = input("Feil velg enten 1 eller 2 eller 3: ")
        if valg6 == "1":
            print("Du ruller med reken og reken virker som den ble glad det virker som du har en venn og stolepå i framtiden. Reken gir deg en stor reke hale som gir deg ekstra defence.")
            Karakteren.plusdefence(0.4)
            venner.append("Storreke")
        elif valg6 == "2":
            print("Reken blir veldig overasket og dytter deg vekk, du får et rekeskjell i beinet og mister dfence. Men du fikk en bit av reken og healer 5 hp og får en ekstra fiskeånde. Du har en følelse at reken vil huske dette i framtiden")
            Fiskeånde += 1
            uvenner.append("Storreke")
            Karakteren.plusdefence(-0.4)
        else:
            print("Du angriper reken")
        ettervulkaninsjø()

                
    else:
        valg7 = input("Du er å toppen av en stor glødene vulkan ønsker du å hoppe oppi(1), danse en reindans på toppen av vulkanen(2), eller offre en random kar som står på den andre siden av krateret av deg?(3) ")
        os.system("cls")
        while valg7 != "1" and valg7 != "2" and valg7 != 3:
            valg7 = input("Feil velg enten 1 eller 2 eller 3: ")
        if valg7 == "1":
            print("Vulkanen rumler godt og fornøyd du får et deigelig varmt bad i magmaen og får fult liv og magma armor + 0.4 defence. og en vulkann venn for livet.")
            venner.append("Vulkan")
            Karakteren.plusdefence(0.4)
            Karakteren.fultliv()
        
        elif valg7 == "2":
            print("Regngudene har hørt ditt bønn og det starter å reine i bøtter og spann. Vulkanen rumler uhyggelig og du lukter en kvalmende lukt av egg. Før vulkanen stivner til og dør tar du 30 dmg av den giftige hevnen til vulkanen.")
            Karakteren.dmg_verden(30)
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
        
        else:
            print("Ingen ting skjer men du hører mannen roppe opp fra vulkanen han virker ikke fornayd han sier at han vil finne deg og ta deg. Vulkanen grynter fornøyd. Du får en ny venn og en ny uvenn!")
            venner.append("Vulkan")
            uvenner.append("Random_kar")
        ettervulkaninsjø()

def ettervulkaninsjø():
    print("Du ser et slott")


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
        skog()

        



   

