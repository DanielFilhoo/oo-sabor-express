from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Dan', 7)
restaurante_praca.receber_avaliacao('Vic', 10)
restaurante_praca.receber_avaliacao('Dani', 15)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()