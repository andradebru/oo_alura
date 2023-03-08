# from conta_classe import Conta
# conta1 = Conta(1, 'Bruna', 100, 2000)
# conta2 = Conta(2, 'Jane Doe', 200)

class Conta:
    def __init__(self, numero, titular, saldo, limite=1000): 
        print(f'Construindo objeto {self}')
        self.__numero = numero # assim como no java se usa a palavra private p limitar a classe, em python usamos 2 underscores no inicio '__'
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # constroi a conta
        # qdo tem um valor padrao pode-se passar no argumento da classe em vez de na criacao do objeto 


    def extrato(self):
        print(f'Titular: {self.__titular} // Saldo: {self.__saldo}')
        # conta1.extrato()


    def deposita(self, valor):
        self.__saldo += valor
        print(f'Titular: {self.__titular} // Voce depositou R$ {valor} e agora seu saldo é de R$ {self.__saldo}')
        # conta1.deposita(20)


    def saca(self, valor):
        self.__saldo -= valor
        print(f'Titular: {self.__titular} // Voce sacou R$ {valor} e agora seu saldo é de R$ {self.__saldo}')
        # conta1.saca(20)


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        # conta2.transfere(10, conta1)


    # metodos para consultar valores do objeto
    # get: eh a convencao pra td metodo q retorna algo
    def get_saldo(self): 
        return self.__saldo
        # conta1.get_saldo()


    def get_titular(self):
        return self.__titular
        # conta1.get_titular()


    def get_limite(self):
        return self.__limite
        # conta1.get_limite()
    
    # metodos para alterar algum valor do objeto
    # set: nunca retorna nada, apenas altera o valor
    def set_limite(self, limite):
        self.__limite = limite
        # conta1.set_limite(10000)

    # agora com os __ antes do atributo, eles seriam chamados no terminal como '_Classe__atributo', 
    # indicando q sao privados e deveriam ser modificados atraves dos metodos-