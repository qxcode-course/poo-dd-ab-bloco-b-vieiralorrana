class Blusa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTam(self):
        return self.__tamanho
    
    def setTam(self, numeracao):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if numeracao not in tamanhos_validos:
            print(f"fail: tamanho não encontrado. tamanhos permitidos: {tamanhos_validos}")
        else:
            self.__tamanho = numeracao


camiseta = Blusa() 
camiseta.setTam("C") 
print(camiseta.getTam())