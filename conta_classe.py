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
        # from conta_classe import Conta
        # conta1 = Conta(1, 'Bruna', 100, 2000)
        # conta1.extrato()

    def deposita(self, valor):
        self.__saldo += valor
        print(f'Voce depositou R$ {valor} e agora seu saldo é de R$ {self.__saldo}')
    
    def saca(self, valor):
        self.__saldo -= valor
        print(f'Voce depositou R$ {valor} e agora seu saldo é de R$ {self.__saldo}')

    # agora com os __ antes do atributo, eles seriam chamados no terminal como '_Classe__atributo', indicando q sao privados 
    # e deveriam ser modificados atraves dos metodos