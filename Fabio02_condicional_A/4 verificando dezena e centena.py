# 4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.

def main():

    valor = int(input('Digite um número de dois digitos: '))
    separar_digitos(valor)

def separar_digitos(numero):
    dezena = numero // 10
    centena = numero % 10

    verificar_digitos(dezena, centena)

def verificar_digitos(dezena, centena):
    if dezena != centena:
        print('O algarismo da dezena é DIFERENTE do algarismo da unidade')
    else:
        print('O algarismo da dezena é IGUAL do algarismo da unidade')


main()
