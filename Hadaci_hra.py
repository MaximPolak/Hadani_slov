def vytiskni_uhodnute_znaky(slovo):
    seznam_uhodnutych_pismen = []
    pokusy = 3
    while pokusy > 0:
        pismeno = input("Zadejte písmeno: ")
        if pismeno in slovo:
            if pismeno not in seznam_uhodnutych_pismen:
                seznam_uhodnutych_pismen.append(pismeno)
        else:
            pokusy -= 1 
    print(seznam_uhodnutych_pismen)

vytiskni_uhodnute_znaky("ahoj")