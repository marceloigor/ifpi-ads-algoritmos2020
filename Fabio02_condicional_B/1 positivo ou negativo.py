# 1. Leia um número e mostre na tela se o número é positivo ou negativo.

def main():
    mensagem()

def mensagem():
    numero = int(input('Digite um número: '))

    posi_neg(numero)

def posi_neg(numero):
    if numero > 0:
        print(f'{numero} é um numero positivo')
        return mensagem()
    elif numero < 0:
        print(f'{numero} é um numero negativo')
        return mensagem()
    else:
        print(f'{numero} é um numero neutro')
        return mensagem()



main()