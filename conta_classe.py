class Conta:
    def __init__(self, numero, titular, saldo, limite=1000): 
        print(f'Construindo objeto {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        # constroi a conta
        # qdo tem um valor padrao pode-se passar no argumento da classe em vez de na criacao do objeto 

    def extrato(self):
        print(f'Titular: {self.titular} // Saldo: {self.saldo}')
        # from conta_classe import Conta
        # conta1 = Conta(1, 'Bruna', 100, 2000)
        # conta1.extrato()

    def deposita(self, valor):
        self.saldo += valor
        print(f'Voce depositou R$ {valor} e agora seu saldo é de R$ {self.saldo}')
    
    def saca(self, valor):
        self.saldo -= valor
        print(f'Voce depositou R$ {valor} e agora seu saldo é de R$ {self.saldo}')
