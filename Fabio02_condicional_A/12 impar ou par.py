# 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar

def main():
    numero = int(input('Digite um número: '))

    impar_par(numero)

def impar_par(numero):
    if numero % 2 == 0:
        print('É par')
    else:
        print('É impar')



main()
