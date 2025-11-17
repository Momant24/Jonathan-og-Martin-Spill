import time




Start = input("Press s og så enter for å starte gamet: ")

if Start == "S" or Start == "s":
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
    
    Førstelevvel = input("Du har 2 valg ønsker du å gå inn i en frydig skog(1) eller gå til en Flyvende øy(2): ")
    while (Førstelevvel != "1" or Førstelevvel != "2"):
        Førstelevvel = input("Feil velg enten 1 eller 2: ")
    if Førstelevvel == 1:
        print("yey")
    else:
        print("du falt ned L")


