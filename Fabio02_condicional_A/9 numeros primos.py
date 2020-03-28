# 9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

def main():
    numero = int(input('Digite um número: '))

    eh_primo(numero)

def eh_primo(numero):
    if numero > 1:
        if (numero % 1) == 0 and (numero % numero) == 0:
            verificar(numero)
    else:
        print('NÃO é primo')

def verificar(numero):
    if numero > 2 and (numero % 2) == 0:
        print('NÃO é primo')
    elif numero > 3 and (numero % 3) == 0:
        print('NÃO é primo')
    elif numero > 5 and ((numero %  10) == 0 or (numero %  10) == 5):
        print('NÃO é primo')
    elif numero > 7 and (numero % 7) == 0:
        print('NÃO é primo')
    else:
        print('É primo')


main()
