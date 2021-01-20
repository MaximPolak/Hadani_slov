import enum

class GameOverError(Exception):
    pass

class Stav(enum.Enum):
    VYHRA = 1
    HRA = 0
    PROHRA = -1

class Kolo:
    def __init__(self, slovo: str, pocet_pokusu: int):
        self._slovo, self._pocet_pokusu = slovo, pocet_pokusu
        self._neuhodnuta_pismena = set(self.slovo)
        self._stav = Stav.HRA
        self.uhodnuta
        
    @property
    def slovo(self):
        return self._slovo

    @property
    def pocet_pokusu(self):
        return self._pocet_pokusu
    @pocet_pokusu.setter
    def pocet_pokusu(self, hodnota):
        self._pocet_pokusu = hodnota

    @property
    def neuhodnuta_pismena(self):
        return self._neuhodnuta_pismena
    @neuhodnuta_pismena.setter
    def neuhodnuta_pismena(self, hodnota):
        self._neuhodnuta_pismena = hodnota

    @property
    def stav(self):
        return self._stav
    @stav.setter
    def stav(self, hodnota):
        self._stav = hodnota
    
    @property
    def uhodnuta(self):
        retezec = ""
        for pismeno in self.slovo:
            retezec += "_" if pismeno in self.neuhodnuta_pismena else pismeno
        return retezec

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
    
    def _uhodni(self, vstup):
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