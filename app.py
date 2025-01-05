from modelos.restaurante import Restaurante

'''
informacoes dos restaurantes
'''
restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_praca.receber_avaliacao("Jose", 4)
restaurante_praca.receber_avaliacao("gus", 5)

restaurante_pizza = Restaurante('pizzaolo', 'FastFood')

restaurante_mexicano = Restaurante('Mexicanito', 'mexicano')

restaurante_mexicano.alternar_estado()

#chamando a funcao da lista de restaurantes
def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()