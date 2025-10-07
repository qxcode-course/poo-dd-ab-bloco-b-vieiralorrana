class Watch:
    def __init__(self):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0

    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minuto 
    
    def getSegundo(self):
        return self.__segundo
    
    def setHora(self, valor: int):
        if valor < 0 or valor > 23:
            print("fail: hora invalida") 
        else:
            self.__hora = valor

    def setMinuto(self, valor: int):
        if valor < 0 or valor > 59:
            print("fail: minuto inválido") 
        else:
            self.__minuto = valor

    def setSegundo(self, valor: int):
        if valor < 0 or valor > 59:
            print("fail: segundo inválido")
        else:
            self.__segundo = valor 

    def show(self) -> None:
        print(self)

    def __str__(self):
        return (f"{self.getHora():.2f}:{self.getMinuto():.2f}:{self.getSegundo():.2f}")
    
    def nextSecond(self):
        if self.getSegundo() == 59:
            self.setSegundo(0)
            self.setMinuto(self.getMinuto() + 1)
        else:
            self.setSegundo(self.getSegundo() + 1)
        
        if self.getMinuto() == 59:
            self.setMinuto(0)
            self.setHora(self.getHora() + 1)
        
        if self.getHora() == 23:
            self.setHora(0)
            self.setSegundo(self.getSegundo() + 1)

def main():
    relogio = Watch()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "set" or "init":
            valor = int(args[1])
            valor2 = int(args[2])
            valor3 = int(args[3])
            relogio.setHora(valor)
            relogio.setMinuto(valor2)
            relogio.setSegundo(valor3)
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "next":
            relogio.nextSecond()
main()    