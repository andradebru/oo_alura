# from cliente import Cliente
# cliente = Cliente("bruna")
# cliente.nome = "bruna"

class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property # com o @property nao precisa chamar o metodo com (), nem ter get_ na frente, pois eh subentendido
    def nome(self):
        return self.__nome.title()
      # cliente.nome

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
        # cliente.nome = "bruna A"
