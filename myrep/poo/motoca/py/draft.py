class Pessoa:
    def __init__(self):
        self.__nome: str = ""
        self.__idade: int 

    def getNome(self):
        return self.__nome
    
    def setNome(self, value):
        self.__nome = value 

    def getIdade(self):
        return self.__idade 
    
    def setIdade(self, value):
        self.__idade = value 
    
    def show(self) -> None:
        print(self)
    
    def __str__(self):
        return f"{self.setNome()}:{self.setIdade()}"

class Moto:
    def __init__(self):
        self.__potencia: int = 1
        self.__passageiro: Pessoa | None
        self.__tempo: int = 0

    def getPotencia(self):
        return self.__potencia

    def getPassageiro(self):
        return self.__passageiro

    def getTempo(self):
        return self.__tempo 
    
    def inserir(self, passageiro: Pessoa) -> bool:
        if self.__passageiro != None:
            print("fail: busy motorcycle")
            return False
        else:
            self.__passageiro = passageiro
            return True 
    
    def show(self) -> None:
        print(self)
    
    def __str__(self):
        return f"power:{self.getPotencia()}, time:{self.getTempo()}, person:{self.getPassageiro()}"
    

def main():
    pessoa = Pessoa() 
    motoca = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(motoca)
        elif args[0] == "init":
            tempo = args[1]
            motoca(tempo) 
        elif args[0] == "enter":
            nome = args[1]
            idade = args[2]
            pessoa = Pessoa(nome, idade)
            motoca.inserir(pessoa)
            
main()

