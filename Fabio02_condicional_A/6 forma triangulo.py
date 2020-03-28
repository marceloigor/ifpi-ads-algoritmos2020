"""
6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180º). Se formam,
verifique se formam um triângulo acutângulo (3 ângulos < 90º), retângulo (1 ângulo = 90º) ou
obtusângulo (1 ângulo > 90º). Não existe ângulo com tamanho 0º (zero grau). 
"""

def main():
    angulo_1 = int(input('Digite o 1º ângulo: '))
    angulo_2 = int(input('Digite o 2º ângulo: '))
    angulo_3 = int(input('Digite o 3º ângulo: '))

    forma_triangulo(angulo_1, angulo_2, angulo_3)

def forma_triangulo(angulo_1, angulo_2, angulo_3):
    if (angulo_1 + angulo_2 + angulo_3) == 180:
        print('forma triângulo')
        tipo_triangulo(angulo_1, angulo_2, angulo_3)
    elif angulo_1 == 0 or angulo_2 == 0 or angulo_3 == 0:
        print('Não existe ângulo com tamanho 0º (zero grau)')
    else:
        print('Não forma triângulo')

def tipo_triangulo(a1, a2, a3):
    if a1 < 90 and a2 < 90 and a3 < 90:
        print('Forma um triângulo acutângulo')
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print('Forma um triângulo retângulo')
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print('Forma um triângulo obtusângulo')




main()
