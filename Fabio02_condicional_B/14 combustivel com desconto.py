"""
14. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
1. Álcool:
    · até 20 litros, desconto de 3% por litro
    · acima de 20 litros, desconto de 5% por litro
2. Gasolina:
    · até 20 litros, desconto de 4% por litro
    · acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

def main():
    mensagem()

def mensagem():
    qtd_litros = float(input('Digite a quantidade em litros do combustivel: '))
    tipo_combustivel = input('Digite o tipo de combustivel: "A"- Álcool e "G"- Gasolina: ')

    valor_pago(qtd_litros, tipo_combustivel)

def valor_pago(qtd_litros, tipo_combustivel):
    if tipo_combustivel == 'A':
        desconto(qtd_litros, tipo_combustivel, 2.50, 3, 5)
    elif tipo_combustivel == 'G':
        desconto(qtd_litros, tipo_combustivel, 1.90, 4, 6)
    else:
        print('Tipo de combustível inválido!')
        return mensagem()

def desconto(qtd_litros, tipo_combustivel, preco, desconto_1, desconto_2):
    valor_total = qtd_litros * preco
    if qtd_litros <= 20.00:
        desconto_combustivel =  (desconto_1 / 100) * valor_total
    else:
        desconto_combustivel =  (desconto_2 / 100) * valor_total
    
    valor_desconto = valor_total - desconto_combustivel
    separador = 40 * '-'
    mostrar = f'\nValor Total               = R$ {valor_total:.2f}\
                \nTipo de Combustível       = {tipo_combustivel}\
                \nPreço do combustível/L    = R$ {preco:.2f}\
                \nDesconto                  = R$ {desconto_combustivel:.2f}\
                \n{separador}\
                \nValor Final               = R$ {valor_desconto:.2f}'
    print(mostrar)



main()