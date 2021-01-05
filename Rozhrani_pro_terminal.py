from Logika import Kolo, GameOverError

hra = Kolo("autobus", 5)

while True:
    print("Hádané slovo: " + hra.ukaz_uhodnuta())
    pokus = input("Zadejte slovo či písmeno: ").lower()
    try:
        if hra.uhodnuti_pismene(pokus) or hra.uhodnuti_slova(pokus):
            print("\n""Správně")
        else:
            print("\n""Špatně")
        
        print("Zbývající počet pokusů:", hra.pocet_pokusu, "\n" + 35 * "-")
    except GameOverError:
        if hra.stav == "VÝHRA":
            print("\n""Vyhráli jste!")    
        else:
            print("\n""Prohráli jste")
        break        