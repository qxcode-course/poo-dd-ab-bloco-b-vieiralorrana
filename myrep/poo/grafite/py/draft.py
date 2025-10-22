class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness 
        self.__size = size

    def getThickness(self):
        return self.__thickness
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size 
    
    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6 
    
    def __str__(self):
        return f"{self.getThickness():.1f}:{self.getHardness()}:{self.getSize()}"
        
class Lapiseira:
    def __init__(self, espessura: float):
        self.__espessura = espessura
        self.__grafite: Grafite | None = None

    def getEspessura(self):
        return self.__espessura
    
    def getGrafite(self):
        return self.__grafite
    
    def temGrafite(self) -> bool:
        if self.__grafite != None:
            return True
        else:
            return False
    
    def inserir(self, grafite: Grafite) -> bool:
        if self.__grafite != None:
            print("fail: ja existe grafite")
            return False
        else:
            if self.getEspessura() != grafite.getThickness():
                print("fail: calibre incompativel")
                return False
            else:
                self.__grafite = grafite 
                return True
    
    def remover(self) -> Grafite | None:
        aux = self.__grafite
        self.__grafite = None
        return aux
    
    def escever(self):
        if self.__grafite == None:
            print("fail: nao existe grafite")
            return 
        if self.__grafite.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        
        uso = self.__grafite.usagePerSheet()
        mm_usavel = self.__grafite.getSize() - 10
        maxFolhas = mm_usavel // uso 

        if maxFolhas <= 0:
            print("fail: folha incompleta")
            return
        
    def __str__(self):
        grafite = f"[{self.__grafite}]" if self.__grafite != None else "null"
        return f"calibre: {self.getEspessura():.1f}, grafite: {grafite}"
    

def main():
    lapiseira = Lapiseira(0)

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Lapiseira(calibre)
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "insert":
            calibre_g = float(args[1])
            espessura = args[2]
            tam = int(args[3]) 
            grafite = Grafite(calibre_g, espessura, tam)
            lapiseira.inserir(grafite)
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escever()

main()