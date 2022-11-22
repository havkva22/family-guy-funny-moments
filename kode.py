#tom kode
class Bil:
    def __init__(self, regnum, merke, modell, eigar):
        self.regnum = regnum
        self.merke = merke
        self.modell = modell
        self.eigar = eigar
class Passering:
    def __init__(self, dato, time, regnum):
        self.dato = dato
        self.time = time
        self.regnum = regnum