# 3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
def main():
    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))
    valor_3 = int(input('Digite o 3º valor: '))

    valor_maior(valor_1, valor_2, valor_3)

def valor_maior(v1, v2, v3):
    if v1 >= v2 and v1 >= v3:
        print(f'{v1} é o maior valor')
    elif v2 >= v1 and v2 >= v3:
        print(f'{v2} é o maior valor')
    elif v3 >= v1 and v3 >= v2:
        print(f'{v3} é o maior valor')


main()