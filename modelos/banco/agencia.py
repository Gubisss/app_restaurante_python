from modelos.banco import Banco

class agencia(Banco)
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero  = numero 