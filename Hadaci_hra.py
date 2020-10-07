def prevedeni_na_retezec(seznam):
    retezec = ""
    for i in seznam:
        retezec += i
    return retezec

def hadaci_hra(slovo):
    slovo = slovo.lower()
    uhodnuta_cast = []
    for i in range(len(slovo)):
        uhodnuta_cast.append("-")
    pokusy = 5
    print(uhodnuta_cast)
    print("Máš", pokusy, "pokusů""\n")
    while pokusy > 0:
        vstup = input("Zadej písmeno či slovo:  ").lower()
        if len(vstup) == len(slovo):
            if vstup == slovo:
                stav = "výhra"
            else:
                stav = "špatně"
        elif len(vstup) == 1:
            if vstup in slovo:
                if vstup in uhodnuta_cast:
                    print("\n""Pozor, toto písmeno si již uhádnul/a!")
                    stav = " "
                else:
                    for pozice, znak in enumerate(slovo):
                        if znak == vstup:
                            uhodnuta_cast[pozice] = vstup
                            stav = "dobře"            
                if prevedeni_na_retezec(uhodnuta_cast) == slovo:
                    stav = "výhra"
            else:
                stav = "špatně"
        else:
            stav = " "
            print("\n""Špatný vstup, zkus zadat znovu!")
        
        #tisknutí dle stavu
        if stav == "výhra":
            print("\n""VYHRÁL/A JSI!")
            break
        elif stav == "dobře":
            print("\n""SPRÁVNĚ")
        elif stav == "špatně":
            pokusy -= 1
            print("\n""ŠPATNĚ")
        else:
            pokusy -= 1
        print("Hádané slovo:", prevedeni_na_retezec(uhodnuta_cast))
        print("Zbývající pokusy:", pokusy, "\n")
    else:
        print("PROHRÁL/A JSI!")

hadaci_hra("autobus")