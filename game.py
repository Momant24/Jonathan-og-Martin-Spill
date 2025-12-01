import time
import os
from random import randint
from classes import Player, Enemy

#variabler for fiender du kan møte i gamet
fiend = Enemy("Orc", 30, 1.5, 0.8, "Pinne", 0)
fiend2 = Enemy("Brennende_Tree", 40, 1.1, 0.9, "Edel_Pinne", 0)
reke = Enemy("Giga_Reke", 60, 1.5, 0.8, "Reke_Sjell", 0)
Ridder = Enemy("Ridder", 40, 1.8, 0.7, "Sverd", 0)
Vokter = Enemy("Vokter", 70, 1.7, 0.67, "Vokter_Pinne", 0)

#Tillfeldig møte på fiender
def randomEncount(karakter, fiende):
    randEnc = randint(1,8)
    if karakter._fiske_onde < 1:
        if randEnc <= 2:
            print(f"Du har møtt på en {fiende._name}!")
            omvant = retryFight(karakter, fiende)
            return omvant
        elif randEnc > 3:
            print(f"{fiende._name} så deg ikke og du slapp unna.")
    else:
        Karakteren._fiske_onde -= 1
        print(f"Din ånde stinker såpass av fisk at {fiende._name} stakk av")

venner = []
uvenner = []

#Funksjoneer for navigasjon i spillet, altså hva som skjer hvert valg spiller tar
def skog():
    global venner
    valg = input("I skogen ser du et stort tre som er i full flamme ønsker du å risikere å bli angrepet ved å slukke treet(1), løpe vekk å gjemme deg(2), eller angripe på forhond?(3) ")
    os.system("cls")
    while valg != "1" and valg != "2" and valg != "3":
        valg = input("Feil velg enten 1 eller 2 eller 3: ")
    if valg == "1":
        print("Sekken din beynner å brenne å du mister 20 hp. Men du redder det gigantiske treet og han gir deg en edel pinne som gjør 10dm og sier at hvis du noen gang trenger hjelp vil han komme til din hjelp!")
        Karakteren.nyvopen("Edel_Pinne")
        Karakteren.dmg_verden(20)
        print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")

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
            Karakteren.dmg_verden(25)
            Karakteren.nyvopen("Svidd_Edel_Pinne")
            print(f"Du her nå {Karakteren._typ} som våpen")
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")



        nytt_sted()
    
    else:
        print("Du kjemper")
        result = retryFight(Karakteren, fiend2)
        if result == "tap":
            skog()
        else:
            print("Du tar edel pinnen fra det døde tret, men føler at trerne rundt deg skygger surt over deg. Du skynter deg ut av skogen")
            Karakteren.nyvopen("Edel_Pinne")
            uvenner.append("Skog")
            print(f"Du her nå {Karakteren._typ} som våpen")
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
            nytt_sted()
       
def nytt_sted():
    time.sleep(3)
    global venner
    global uvenner

    valg3 = input("Du ser en vakker insjø(1), og en stor glødene vulkan(2). Hvor vil du gå?: ")
    os.system("cls")
    while valg3 != "1" and valg3 != "2":
        valg3 = input("Feil velg enten 1 eller 2: ")

    if valg3 == "1":
        result = randomEncount(Karakteren, fiend)
        valg4 = input("Til venstre ser du insjøen dele seg i to som jesus står gjemt bak et tre og holder veien framover åpen for deg(1), eller ønsker du å ungå denne tråldommen og svømme over, du skimter små fisk i vannet(2): ")
        os.system("cls")
        while valg4 != "1" and valg4 != "2":
            valg4 = input("Feil velg enten 1 eller 2: ")
        if valg4 == "1":
            print("Du beveger deg usikker bortover den våte bunnen av insjøen med vannet stigende over deg på hvær sin side når en fisk flyr ut av den ene veggen rett inn i munnen din. Du føler deg god og mett og får 10 hp og en ånde stinkende av fisk")
            Karakteren.dmg_verden(-10)
            print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
            Karakteren._fiske_onde += 1
           
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
            print("Reken blir veldig overasket og dytter deg vekk, du får et rekesjell i beinet og mister dfence. Men du fikk en bit av reken og healer 5 hp og får en ekstra fiskeånde. Du har en følelse at reken vil huske dette i framtiden")
            Karakteren._fiske_onde += 1
            uvenner.append("Storreke")
            Karakteren.plusdefence(-0.4)
        else:
            print("Du angriper reken")

            result = retryFight(Karakteren, reke)
            if result == "tap":
                nytt_sted()
            else:
                print("Du tar reken sin hale og rekesjell som våpen 14dm. Du bruker halen som armor det gir deg pluss 0.5 dfence")
                Karakteren.plusdefence(0.4)
                Karakteren.nyvopen("Reke_Sjell")
                print(f"Du her nå {Karakteren._typ} som våpen")
                print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
                
        ettervulkaninsjø()

                
    else:
        valg7 = input("Du er å toppen av en stor glødene vulkan ønsker du å hoppe oppi(1), danse en reindans på toppen av vulkanen(2), eller offre en random kar som står på den andre siden av krateret av deg?(3) ")
        os.system("cls")
        while valg7 != "1" and valg7 != "2" and valg7 != "3":
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
    time.sleep(1)
    print("Du går mot slottet")
    time.sleep(2)
    print("Du går inn i slottet")
    time.sleep(3)
    print("Er ikke dette spennende")
    o = input("SI JA")
    os.system("cls")
    if o.lower() == "ja":
        pass
    else:
        print("Det er spennende, du er bare kjedelig")
    time.sleep(1)
    print("Du går bortover gangen")
    time.sleep(1)
    result = randomEncount(Karakteren, Ridder)
    if result == "vant":
        Karakteren.nyvopen("Sverd")
        Karakteren.plusdefence(0.2)
        Karakteren.fultliv()
        result = None
        print(f"Du her nå {Karakteren._typ} som våpen")
        print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
    input("Du går opp en trapp. (Trykk enter)")
    os.system("cls")
    result = randomEncount(Karakteren, Ridder)
    if result == "vant":
        Karakteren.nyvopen("Sverd")
        Karakteren.plusdefence(0.2)
        Karakteren.fultliv()
        result = None
        print(f"Du her nå {Karakteren._typ} som våpen")
        print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
    input("Du går bortover enda en gang (trykk enter): ")
    os.system("cls")
    result = randomEncount(Karakteren, Ridder)
    if result == "vant":
        Karakteren.nyvopen("Sverd")
        Karakteren.plusdefence(0.2)
        Karakteren.fultliv()
        result = None
        print(f"Du her nå {Karakteren._typ} som våpen")
        print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
    input("Du går mot to kjempestore dører. Enter: ")
    os.system("cls")
    result = randomEncount(Karakteren, Vokter)
    if result == "vant":
        Karakteren.nyvopen("Vokter_Pinne")
        Karakteren.plusdefence(0.2)
        Karakteren.fultliv()
        result = None
        print(f"Du har nå {Karakteren._typ} som våpen")
        print(f"Du har nå {Karakteren.liv_igjenn()} hp igjenn")
    input("Du sniker deg gjennom de to dørene. På den andre siden ser du et kjempemonster av alle dine uvenner. Du blåser i hornet ditt og vennene dine kommer: ")
    os.system("cls")
    Karakteren.fultliv()
    for i in venner:
        if i == "Storttree":
            Karakteren.dmg_verden(-60)
            print("Vennen ditt treet møtter opp og gir deg 60 mer hp")
            time.sleep(2)
        elif i == "Storreke":
            Karakteren.midlertidigdmg(6)
            print("Vennen ditt Storreke møtter opp og gir deg 6 mer dmg")
            time.sleep(2)
        elif i == "Vulkan":
            print("Vennen ditt Vulkanen møtter opp og gir deg 0.5 mer dfence")
            Karakteren.plusdefence(0.5)
            time.sleep(2)
    print(Karakteren)
    fiendedmg = 18
    fiendehp = 100
    fiendedefence = 2
    time.sleep(2)
    for i in uvenner:
        if i == "Skog":
            print("Din uvenn skogen dukket opp og merga med kongen +40 hp")
            fiendehp += 35
            time.sleep(2)
        elif i == "Storreke":
            print("Din uvenn Megareken dukket opp og merga med kongen +0,4 dfence")
            fiendedefence += 0.4
            time.sleep(2)
        elif i == "Random_kar":
            print("Din uvenn Random_Kar dukket opp og merga med kongen +6 dmg")
            fiendedmg += 6
            time.sleep(2)

    input("Er du klar for å kjempe?: ")
    Konge = Enemy("Konge_og_Finder_Blanding", fiendehp, fiendedefence, 0.5, "Mutant hender", fiendedmg)
    result4 = retryFight(Karakteren, Konge)
    if result4 == "tap":
        print("Du tapte trist")
    else:
        print("Du vant og uvennene dine er døde wohhhooooo")

                



            


    
    
    


#funksjoner for dmg og combat, attakc og healing funksjoner er i sine respektive klasser

#funksjon for skade på fiende
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
            if fiende._hp >= fiende._maxHp:
                print(f"\n{fiende._name} Angriper")
                PlayerDmg_taken(karakter, fiende)
            else:
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
   

#funksjonen som skal kalles for å kunne gå inn i combat med muligheten for å kunne prøve på nytt igjen
def retryFight(karakter, fiende):
    matchCount = 0
    while True:
        kjemper(karakter, fiende)
        matchCount += 1
        if karakter._hp > 0:
            
            if matchCount == 1:
                print(f" \n gratulerer, du drepte {fiende._name}!")
                return "vant"
            elif matchCount == 2:
                print(f" {karakter._name}, {karakter._name}, {karakter._name}, hvordan klarte du det ikke på første forsøk?? {time.sleep(0.2)} \n {fiende._name} er lett å drepe...")
                return "vant"
            elif matchCount == 3:
                print(" Du overlevde. Det tok deg noen forsøk da. kanskje du har tatt feil valg til nå... ")
                return "vant"
            elif matchCount > 3:
                print(f"avslutter kamp... {time.sleep(0.3)} \n {karakter._name}, du skuffer... \n {matchCount} forsøk, du er ASSS")
                return "vant"
                
            break
            
        else: 
            b = input(" Prøve igjen? eller er du for dårlig for det? \n j/n?:")
            if b.lower() == "j":
                karakter._hp = karakter._maxHp
                fiende._hp = fiende._maxHp
            else: 
                print(f"avslutter kamp... {time.sleep(0.3)} \n {karakter._name}, du skuffer...")
                return "tap"
                

#start spillet
Start = input("Press s og så enter for å starte gamet: ")
os.system("cls")

if Start.lower() == "s":
    print("Starter spill")
    for i in range(2):
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

