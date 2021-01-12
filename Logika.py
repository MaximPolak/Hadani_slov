import enum

class GameOverError(Exception):
    pass

class Stav(enum.Enum):
    VYHRA = 1
    HRA = 0
    PROHRA = -1

class Kolo:
    def __init__(self, slovo: str, pocet_pokusu: int):
        self.slovo, self.pocet_pokusu = slovo, pocet_pokusu
        self.neuhodnuta_pismena = set(self.slovo)
        self.stav = Stav.HRA
        
    def ukaz_uhodnuta(self) -> str:
        retezec = ""
        for pismeno in self.slovo:
            retezec += "_" if pismeno in self.neuhodnuta_pismena else pismeno
        return retezec

    def hraje_se(self) -> None:
        if self.stav != Stav.HRA:
            raise GameOverError

    def obnov_stav(self) -> None:
        if not self.neuhodnuta_pismena:
            self.stav = Stav.VYHRA
        elif self.pocet_pokusu == 0:
            self.stav = Stav.PROHRA
    
    def uhodni(self, vstup):
        self.hraje_se()
        if len(vstup) != 1 and len(vstup) != len(self.slovo):
            raise ValueError("špatný vstup")
        self.hraje_se()
        if len(vstup) == 1:
            
            if vstup in self.slovo:
                self.neuhodnuta_pismena.discard(vstup)
                uspech = True
            else:
                uspech = False
        else:
            if vstup == self.slovo:
                self.neuhodnuta_pismena.clear()
                uspech = True
            else:
                
                uspech = False

        if not uspech:
            self.pocet_pokusu -= 1
        self.obnov_stav()
        return uspech