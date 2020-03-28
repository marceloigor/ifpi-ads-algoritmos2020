# 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.

def main():
    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))
    valor_3 = int(input('Digite o 3º valor: '))
    valor_4 = int(input('Digite o 4º valor: '))
    valor_5 = int(input('Digite o 5º valor: '))

    valor_maior(valor_1, valor_2, valor_3, valor_4, valor_5)

def valor_maior(v1, v2, v3, v4, v5):
    maior = 0
    menor = 0
    if v1 > v2 and v1 > v3 and v1 > v4 and v1 > v5:
        maior = v1
        menor = valor_menor(v2, v3, v4, v5)
    elif v2 > v1 and v2 > v3 and v2 > v4 and v2 > v5:
        maior = v2
        menor = valor_menor(v1, v3, v4, v5)
    elif v3 > v1 and v3 > v2 and v3 > v4 and v3 > v5:
        maior = v3
        menor = valor_menor(v1, v2, v4, v5)
    elif v4 > v1 and v4 > v2 and v4 > v3 and v4 > v5:
        maior = v4
        menor = valor_menor(v1, v2, v3, v5)
    else:
        maior = v5
        menor = valor_menor(v1, v2, v3, v4)

    print(f'O maior valor é {maior}, e o menor é {menor}.')

def valor_menor(p1, p2, p3, p4):
    menor = 0
    if p1 < p2 and p1 < p3 and p1 < p4:
        menor = p1
    elif p2 < p1 and p2 < p3 and p2 < p4:
        menor = p2    
    elif p3 < p1 and p3 < p2 and p3 < p4:
        menor = p3  
    else:
        menor = p4
    return menor


main()
