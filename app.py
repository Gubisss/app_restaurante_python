from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

'''
informacoes dos restaurantes
'''
restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Melancia', 1.0, '500ml')
bebida_suco.aplicar_desconto()
prato_dia = Prato('macarrao', 25, 'ao sugo')
prato_dia.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_dia)


# restaurante_praca.receber_avaliacao("Jose", 4)
# restaurante_praca.receber_avaliacao("gus", 5)

# restaurante_pizza = Restaurante('pizzaolo', 'FastFood')

# restaurante_mexicano = Restaurante('Mexicanito', 'mexicano')

# restaurante_mexicano.alternar_estado()

# chamando a funcao da lista de restaurantes
def main():
    restaurante_praca.exibir_cardapio
#     Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()