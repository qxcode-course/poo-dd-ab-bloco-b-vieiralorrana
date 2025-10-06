class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTam(self):
        return self.__tamanho
    
    def setTam(self, valor: int):
        if valor < 20 or valor > 50 or valor % 2 != 0:
            print("fail: tamanho invalido")
        else:
            self.__tamanho = valor

    def show(self) -> None:
        print(self)
    
    def __str__(self): 
        return (f"O tamanho da minha chinela é: {self.getTam()}")

def main():
    chinela = Chinela()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        
        if args[0] == "end":
            break
        elif args[0] == "init":
            valor = int(args[1])
            chinela.setTam(valor)
        elif args[0] == "show":
            print(chinela)

main()
            