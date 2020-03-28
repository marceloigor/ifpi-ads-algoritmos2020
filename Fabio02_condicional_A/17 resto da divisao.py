"""
17. Leia valores inteiros em duas variáveis distintas e 
se o resto da divisão da primeira pela segunda for 1 escreva a soma dessas variáveis mais o resto da divisão;
se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares;
se for igual a 3 multiplique a soma dos valores lidos pelo primeiro;
se for igual a 4 divida a soma dos números lidos pelo segundo, se este for diferente de zero.
Em qualquer outra situação escreva o quadrado dos números lidos.
"""

def main():
    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))
    
    soma = valor_1 + valor_2
    resto = valor_1 % valor_2
    print(f'Resto = {resto}')

    if resto == 1:
        print(f'A soma dessas variáveis mais o resto da divisão = {soma + resto}')
    elif resto == 2:
        impar_par(valor_1)
        impar_par(valor_2)
    elif resto == 3:
        print(f'multiplicação da soma dos valores lidos pelo primeiro = {soma * valor_1}')
    elif resto == 4:
        divi = soma / valor_2
        if divi == 0:
            print(f'divisão da soma dos números lidos pelo segundo = {divi}')
        else:
            quadrado(valor_1)
            quadrado(valor_2)
    else:
        quadrado(valor_1)
        quadrado(valor_2)

def impar_par(numero):
    if numero % 2 == 0:
        print(f'{numero}É par')
    else:
        print(f'{numero}É impar')

def quadrado(valor):
    quadrado_num = valor ** 2
    print(f'O quadrado dos números lidos = {quadrado_num}')


main()
