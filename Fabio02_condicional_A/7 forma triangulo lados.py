"""
7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero). 
"""

def main():

    lado_1 = int(input('Digite o 1º lado: '))
    lado_2 = int(input('Digite o 2º lado: '))
    lado_3 = int(input('Digite o 3º lado: '))

    forma_triangulo(lado_1, lado_2, lado_3)

def forma_triangulo(a, b, c):
    if a == 0 or b == 0 or c == 0:
        print('Não existe lado com tamanho 0 (zero)')
    elif (a + b) >= c and (a + c) >= b and (b + c) >= a:
        print('Forma triângulo')
        tipo_triangulo(a, b, c)
    else:
        print('Não forma triângulo')

def tipo_triangulo(a, b, c):
    if a == b and b == c:
        print('Forma um triângulo equilátero')
    elif (a == b and b != c) or (a == c and c != b) or (c == b and b != a):
        print('Forma um triângulo isósceles')
    elif a != b and a != c and b !=c:
        print('Forma um triângulo escaleno')
    



main()
