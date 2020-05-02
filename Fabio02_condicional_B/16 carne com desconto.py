"""
16. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
            Até 5 Kg            Acima de 5 Kg
File        R$ 4,90 por Kg      R$ 5,80 por Kg
Alcatra     R$ 5,90 por Kg      R$ 6,80 por Kg
Picanha     R$ 6,90 por Kg      R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

def main():
    mensagem()

def mensagem():
    print('Tipo | 1- File | 2- Alcatra | 3- Picanha |')
    tipo_carne =  input('Digite a carne que deseja: ')
    qtd_carne = float(input('Digite a quantidade (em Kg) que deseja: '))

    valor_carne(tipo_carne, qtd_carne)

def valor_carne(tipo_carne, qtd_carne):
    if tipo_carne == 'File':
        desconto_carne(tipo_carne,qtd_carne, 4.90, 5.80)
    elif tipo_carne == 'Alcatra':
        desconto_carne(tipo_carne,qtd_carne, 5.90, 6.80)
    elif tipo_carne == 'Picanha':
        desconto_carne(tipo_carne,qtd_carne, 6.90, 7.80)
    else:
        print('Tipo de carne inválido!')
        return mensagem()

def desconto_carne(tipo_carne,qtd_carne, preco_1, preco_2):
    if qtd_carne <= 5:
        valor_total = qtd_carne * preco_1
        s_n = input('É no cartão Tabajara? S/N: ')
        if cartao(s_n) == True:
            desconto_cartao = (5 / 100) * valor_total
        else:
            desconto_cartao = 0.0

        valor_final = valor_total - desconto_cartao
    else:
        valor_total = qtd_carne * preco_2
        s_n = input('É no cartão Tabajara? S/N: ')
        if cartao(s_n) == True:
            desconto_cartao = (5 / 100) * valor_total
        else:
            desconto_cartao = 0.0

        valor_final = valor_total - desconto_cartao

    print('\n'15 * '*', 'CUPOM FISCAL', 15 * '*')
    mostrar = f'\nTipo                    = {tipo_carne}\
                \nQuantidade de carne     = R$ {qtd_carne} Kg\
                \nPreço total             = R$ {valor_total:.2f}\
                \nFoi no cartão?          = {s_n}\
                \nValor do desconto       = R$ {desconto_cartao:.2f}\
                \n--------------------------------------------\
                \nValor a pagar           = R$ {valor_final:.2f}'
    print(mostrar)
    
def cartao(valor):
    if valor == 'S' or valor == 's':
        return True
    elif valor == 'N' or valor == 'n':
        return False  


main()