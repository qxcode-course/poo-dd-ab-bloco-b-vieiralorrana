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
            print("fail: minuto invalido") 
        else:
            self.__minuto = valor

    def setSegundo(self, valor: int):
        if valor < 0 or valor > 59:
            print("fail: segundo invalido")
        else:
            self.__segundo = valor 

    def show(self) -> None:
        print(self)

    def __str__(self):
        return (f"{self.getHora():02d}:{self.getMinuto():02d}:{self.getSegundo():02d}")
    
    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo = 0
            self.__minuto == 1
        if self.__minuto == 60:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora == 24:
            self.__hora = 0

def main():
    relogio = Watch()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "set" or args[0] == "init":
            valor = int(args[1])
            valor_2 = int(args[2])
            valor_3 = int(args[3])
            relogio.setHora(valor)
            relogio.setMinuto(valor_2)
            relogio.setSegundo(valor_3)
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "next":
            relogio.nextSecond()

main()