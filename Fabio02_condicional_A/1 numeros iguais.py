# 1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
def main():
    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))
    valor_3 = int(input('Digite o 3º valor: '))

    resultado = numeros_iguais(valor_1, valor_2, valor_3)

def numeros_iguais(v1, v2, v3):
    if v1 == v2 and v1 == v3:
        qtd_iguais(3, v1, v2, v3)
    elif v1 == v2 or v1 == v3 or v2 == v3:
        qtd_iguais(2, v1, v2, v3)
    else:
        qtd_iguais(0, v1, v2, v3)


def qtd_iguais(qtd, v1, v2, v3):
    print(f'Existe {qtd} número(s) iguais entre os números {v1}, {v2} e {v3}')   


main()