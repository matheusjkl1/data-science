from abc import ABC, abstractmethod


class PrintTeste(ABC):
    def __init__(self, stringPrint):
        self.stringPrint = stringPrint

    @abstractmethod
    def printStrMethod(self):
        raise NotImplementedError


class testeClass(PrintTeste):
    def printStrMethod(self):
        print(self.stringPrint)


callFunction = testeClass('teste')

callFunction.printStrMethod()
