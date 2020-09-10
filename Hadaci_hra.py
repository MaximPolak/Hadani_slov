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
        vstup = input("Zadejte písmeno či slovo:  ").lower()
        if len(vstup) == len(slovo):
            if vstup == slovo:
                print("VYHRÁL JSI!")
                break
            else:
                pokusy -= 1
                print("Zbývající pokusy:", pokusy)
        elif len(vstup) == 1:
            if vstup in slovo:
                for pozice, znak in enumerate(slovo):
                    if znak == vstup:
                        uhodnuta_cast[pozice] = vstup
                        print("DOBŘE!")
                        print(uhodnuta_cast)
                if prevedeni_na_retezec(uhodnuta_cast) == slovo:
                    print("VYHRÁL JSI!")
                    break
            else:
                pokusy -= 1
                print("ŠPATNĚ!")
                print("Zbývající pokusy:", pokusy)
        else:
            print("ŠPATNÝ VSTUP, ZKUS ZADAT ZNOVU")
    else:
        print("PROHRÁL JSI!")

vytiskni_uhodnute_znaky("ahoj")