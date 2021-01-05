class GameOverError(Exception):
    pass

class Kolo:
    def __init__(self, slovo: str, pocet_pokusu: int, stav="HRA"):
        self.slovo, self.pocet_pokusu = slovo, pocet_pokusu
        self.neuhodnuta_pismena = set(self.slovo)
        self.stav = stav
    def uhodnuti_pismene(self, pismeno: str) -> bool:
        if len(pismeno) != 1:
            return None
        if pismeno in self.slovo:
            self.neuhodnuta_pismena.discard(pismeno)
            self.obnov_stav()
            self.hraje_se()
            return True
        else:
            self.pocet_pokusu -= 1  
            self.obnov_stav()
            self.hraje_se()
            return False
        
    def ukaz_uhodnuta(self) -> str:
        retezec = ""
        for pismeno in self.slovo:
            retezec += "_" if pismeno in self.neuhodnuta_pismena else pismeno
        return retezec
    def uhodnuti_slova(self, slovo) -> bool:
        if len(slovo) == 1:
            return None
        if slovo == self.slovo:
            self.neuhodnuta_pismena.clear()
            self.obnov_stav()
            self.hraje_se()
            return True
        else:
            self.pocet_pokusu -= 1
            self.obnov_stav()
            self.hraje_se()
            return False

    def hraje_se(self):
        if self.stav != "HRA":
            raise GameOverError
    def obnov_stav(self):
        if self.neuhodnuta_pismena == set():
            self.stav = "VÝHRA"
        elif self.pocet_pokusu == 0:
            self.stav = "PROHRA"