from modelos.avaliacao import Avaliacao 

class Restaurante:
'''
Classe de restaurante
'''
#Inicio da lista 
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

'''
Mostrando as informacoes
'''
    @classmethod
    def listar_restaurantes(cls): 
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria do restaurante".ljust(25)} | {"Status".ljust(25)} | {"media".ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}')

''''
Metodo que define se ele esta ativo ou nao
'''
    @property
    def ativo(self):
        return "verdadeiro" if self._ativo else "Falso"

    def alternar_estado(self):
        self._ativo = not self._ativo

'''
metodo de receber as avaliacoes
'''

    def receber_avaliacao(self, client, nota):
        if nota > 5:
            return print("nota invalida digite ate 5")
        avaliacao = Avaliacao(client, nota)
        self._avaliacao.append(avaliacao)

'''
propriedade de calcular a media das notas das avaliacoes
'''
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 5
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
