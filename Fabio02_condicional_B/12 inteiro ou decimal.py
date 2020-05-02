"""
12. Leia um número e escreva se o número é inteiro ou decimal.
"""

def main():
    mensagem()

def mensagem():
    numero = input('Digite um número: ')

    int_float(numero)

def int_float(numero):
    decimal = float(numero)
    convertido = str(decimal)

    if numero == convertido:
        print('Decimal')
    else:
        print('Inteiro')


main()