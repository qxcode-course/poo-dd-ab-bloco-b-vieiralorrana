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

    def show(self) -> None:
        print(self)
    
    def __str__(self):
        return (f"minha blusa é {self.getTam()}")

def main():
    blusa = Blusa()

    while True:
        print("Qual o tamanho da sua blusa?")
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            numeracao = args[1]
            blusa.setTam(numeracao)
        elif args[0] == "show":
            print(blusa)

main()