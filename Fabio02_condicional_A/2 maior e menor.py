# 2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
def main():

    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))

    valor_maior_menor(valor_1, valor_2)

def valor_maior_menor(v1, v2):
    if v1 > v2:
        print(f'{v1} é MAIOR que {v2}')
    elif v1 < v2:
        print(f'{v1} é MENOR que {v2}')
    else:
        print(f'{v1} é IGUAL a {v2}')

main()
