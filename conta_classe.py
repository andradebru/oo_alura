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

    def pode_sacar(self, valor_saque):
        saque_disponivel =  self.__saldo + self.__limite
        return valor_saque <= saque_disponivel

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
            print(f'Titular: {self.__titular} // Voce sacou R$ {valor} e agora seu saldo é de R$ {self.__saldo}')
        else:
            print(f'O valor R$ {valor} ultrapassa o limite.')
        # conta1.saca(20)


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        # conta2.transfere(10, conta1)


    # metodos para consultar valores do objeto
    # get: eh a convencao pra td metodo q retorna algo
    # com as properties nao precisamos mais declarar get ou set no inicio
    @property
    def saldo(self): 
        return self.__saldo
        # conta1.get_saldo()

    @property
    def titular(self):
        return self.__titular
        # conta1.get_titular()

    @property
    def limite(self):
        return self.__limite
        # conta1.limite
    
    # metodos para alterar algum valor do objeto
    # set: nunca retorna nada, apenas altera o valor
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        # conta1.limite = 2000

    # agora com os __ antes do atributo, eles seriam chamados no terminal como '_Classe__atributo', 
    # indicando q sao privados e deveriam ser modificados atraves dos metodos-