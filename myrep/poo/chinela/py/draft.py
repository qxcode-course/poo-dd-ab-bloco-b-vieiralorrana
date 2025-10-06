class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTam(self):
        return self.__tamanho
    
    def setTam(self, valor: int):
        if valor < 20 or valor > 50 and valor % 2 != 0:
            print("fail: tamanho invalido")
        else:
            self.__tamanho = valor

def main():
    chinela = Chinela()

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line
        
        if args[0] == "init":
            valor = args[1]
            chinela.setTam(valor)

main()
            