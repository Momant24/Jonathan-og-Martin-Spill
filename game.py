import time
from random import randint
from classes import Player, Enemy

fiend = Enemy("Orc", 75, 1.5, 0.5, "pinne", 0)
Karakteren = Player("Bartin", 100, 1.1, 0.5, "Polearm", 0)
def randomEncount(karakter, fiende):
    randEnc = randint(1,3)
    if randEnc >= 2:
        print(f"Du har møtt på en {fiende._name}!")
        retryFight(karakter, fiende)
    elif randEnc < 2:
        print(f"{fiende._name} så deg ikke og du slapp unna.")
        

    
def skog():
    valg = input("I skogen ser du et stort tre som er i full flamme ønsker du å risikere å bli angrepet ved å slukke treet(1), løpe vekk å gjemme deg(2), eller angripe på forhond?(3) ")
    while valg != "1" and Førstelevvel != "2" and Førstelevvel != "3":
        valg = input("Feil velg enten 1 eller 2 eller 3: ")
    if valg == "1":
        print("Sekken din beynner å brenne å du mister 20 hp. Men du redder det gigantiske treet og han gir deg en edel pinne som gjør 5dm og sier at hvis du noen gang trenger hjelp vil han komme til din hjelp!")
        Karakteren.nyvopen("Edel_Pinne")
        print(f"Du her nå {Karakteren._typ} som våpen")
        nytt_sted()

    elif valg == "2":
        print("Du glmete baggen din i all hast og mistet pinnen din. Du finner en ny pinne på bakken men den ser tørr og skjør ut og vil bare ta 1 dm istede for di gamle 2")
        Karakteren.nyvopen("Skjor_Pinne")
        print(f"Du her nå {Karakteren._typ} som våpen")
        nytt_sted()
    
    else:
        print("Du kjemper")
        
        nytt_sted()
    
def nytt_sted():
    print("Hei")
    
    
def EnmyDmg_taken(fiende, karakter):
    fiende._hp -= Player.attack(karakter, fiende)
    if fiende._hp > 0:
        print(f"{fiende._name} har {fiende._hp} hp igjen")
    elif fiende._hp <= 0:
        fiende._hp = 0
        print(f"{fiende._name} har {fiende._hp} hp igjen \n \n")
    
        #funksjon for skade på spiller
def PlayerDmg_taken(karakter, fiende):
    karakter._hp -= Enemy.attack(fiende, karakter)
    if karakter._hp > 0:
        print(f"{karakter._name} har {karakter._hp} hp igjen \n \n")
    elif karakter._hp < 0:
        karakter._hp = 0

def waitAnim(a):
    for i in range(int(a)):
        print("*", end="\r")
        time.sleep(0.5)
        print(" *", end="\r")
        time.sleep(0.5)
        print("  *", end="\r") 
        time.sleep(0.5)
        print("   *", end="\r") 
        time.sleep(0.5)
        print("    ", end="\r")

#fuknsjon for combat
def kjemper(karakter, fiende):
    print(" Du er blitt angrepet!")
    time.sleep(0.5)
    print(f" Din fiende er en {fiende._name}")
    print(fiende)


    
    while karakter._hp > 0 and fiende._hp > 0:   
        #valg av handlinger
        time.sleep(1)
        print("\n Dine valg!")
        print(" 1: angrip \n 2: helbred deg selv \n 3: Ryggsekk")

        # spiller sin tur
        time.sleep(0.1)
        while True:
            print(f"Hva velger du å gjøre?:")

            a = input("\n")
            
            if a == "1":
                EnmyDmg_taken(fiende, karakter) 
                break    
            elif a == "2":
                karakter.playerHeal()
                break
            elif a == "3":
                print("\n dust du har ikke en ryggsekk ennå \n Prøv igjen: \n Dine valg! \n 1: angrip \n 2: Helbred degselb \n 3: ryggsekk")
                continue
            else:
                print(" Ugyldig valg, prøv igjen: \n\n Dine valg! \n 1: angrip \n 2: Helbred degselb \n 3: ryggsekk")
                continue
        time.sleep(1)
        
        
        # stoppe loop hvis fienden er død
        if fiende._hp <= 0:
            break
        
        #Fiende sin tur
        chance = randint(1,20)
        if chance > 15:
            fiende.enemyrHeal()
        else:
            print(f"\n{fiende._name} Angriper")
            PlayerDmg_taken(karakter, fiende)
        
        #stoppe loop hvis spiller er død
        if karakter._hp <= 0:
            break
        # hivs du vinner combat
    if karakter._hp <= 0:  
        print(f"{karakter._name} døde, hva er det du gjør?")
        
    elif fiende._hp <= 0:       
         print(f"{fiende._name} er død, du vant!")   
        
def retryFight(karakter, fiende):
    matchCount = 0
    while True:
        kjemper(karakter, fiende)
        
        if karakter._hp > 0:
            if matchCount == 1:
                print(f" \n gratulerer, du drepte {fiende._name}!")
            elif matchCount == 2:
                print(f" {karakter._name}, {karakter._name}, {karakter._name}, hvordan klarte du det ikke på første forsøk?? {time.sleep(0.2)} \n {fiende._name} er lett å drepe...")
            elif matchCount == 3:
                print(" Du overlevde. Det tok deg noen forsøk da. kanskje du har tatt feil valg til nå... ")
            elif matchCount < 3:
                print(f"avslutter kamp... {time.sleep(0.3)} \n {karakter._name}, du skuffer... \n {matchCount} forsøk, du er ASSS")
                break
            break
            
        else: 
            b = input(" Prøve igjen? eller er du for dårlig for det? \n j/n?:")
            if b.lower() == "j":
                karakter._hp = karakter._maxHp
                fiende._hp = fiende._maxHp
            else: 
                print(f"avslutter kamp... {time.sleep(0.3)} \n {karakter._name}, du skuffer...")
                break
randomEncount(Karakteren, fiend)
Start = input("Press s og så enter for å starte gamet: ")

if Start.lower() == "s":
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
        skog()

        



   

