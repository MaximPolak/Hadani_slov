def prevedeni_na_retezec(seznam):
    retezec = ""
    for i in seznam:
        retezec += i
    return retezec

def vytiskni_uhodnute_znaky(slovo):
    uhodnuta_cast = []
    for i in range(len(slovo)):
        uhodnuta_cast.append("-")
    pokusy = 5
    while pokusy > 0:
        vstup = input("Zadej písmeno či slovo:  ").lower()
        if len(vstup) == len(slovo):
            if vstup == slovo:
                print("VYHRÁL/A JSI!")
                break
            else:
                pokusy -= 1
                print("ŠPATNĚ!")
        elif len(vstup) == 1:
            if vstup in slovo:
                for pozice, znak in enumerate(slovo):
                    if znak == vstup:
                        uhodnuta_cast[pozice] = vstup
                        print("DOBŘE!")
                        
                if prevedeni_na_retezec(uhodnuta_cast) == slovo:
                    print("VYHRÁL/A JSI!")
                    break
            else:
                pokusy -= 1
                print("ŠPATNĚ!")
        else:
            print("ŠPATNÝ VSTUP, ZKUS ZADAT ZNOVU")
        print(uhodnuta_cast)
        print("Zbývající pokusy:", pokusy, "\n")
    else:
        print("PROHRÁL/A JSI!")

vytiskni_uhodnute_znaky("ahoj")