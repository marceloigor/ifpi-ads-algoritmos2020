"""
15. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
            Até 5 Kg            Acima de 5 Kg
Morango     R$ 2,50 por Kg      R$ 2,20 por Kg
Maçã        R$ 1,80 por Kg      R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

def main():
    mensagem()

def mensagem():
    qtd_morango = float(input('Digite a quantidade (em Kg) de morangos: '))
    qtd_maca = float(input('Digite a quantidade (em Kg) de maças: '))

    valor(qtd_morango, qtd_maca)

def valor(qtd_morango, qtd_maca):
    if qtd_morango <= 5.0:
        print(15*'*', 'MORANGOS', 15*'*')
        desconto(qtd_morango, 2.50)
    else:
        print(15*'*', 'MORANGOS', 15*'*')
        desconto(qtd_morango, 2.20)

    if qtd_maca <= 5.0:
        print(15*'*', 'MAÇAS', 15*'*')
        desconto(qtd_maca, 1.80)
    else:
        print(15*'*', 'MAÇAS', 15*'*')
        desconto(qtd_maca, 1.50)       

def desconto(qtd, preco):
    valor_fruta = qtd * preco
    if valor_fruta > 25.00:
        descontos = (10 / 100) * valor_fruta
    else:  
        descontos = 0.0

    valor_final = valor_fruta - descontos
    
    separador = 40 * '-'
    mostrar = f'Valor Total               = R$ {valor_fruta:.2f}\
                \nPreço da fruta por Kg     = R$ {preco:.2f}\
                \nQuantidade                = {qtd} Kg\
                \n{separador}\
                \nDescontos                 = R$ {descontos:.2f}\
                \nValor Final               = R$ {valor_final:.2f}\
                \n{separador}\n'
    print(mostrar)




main()