"""
28. Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
não pode ser negativo.
"""

def main():
    mensagem()

def mensagem():
    x1, y1 = map(int, input('Digite os dois valores de (x e y) do 1º ponto: ').split(', '))
    x2, y2 = map(int, input('Digite os dois valores de (x e y) do 2º ponto: ').split(', '))

    maior_0(x1, x2, y1, y2)

def area_retangulo(x1, x2, y1, y2):
    a = x1 - x2
    b = y1 - y2
    if x1 < x2 and y1 < y2:
        if x2 != y2 and x2 != y1 and a != b:
            area = a * b
            print(f'A área do retangulo = {area}.')
        else:
            print('As coordenadas não formam um retângulo.')
            return mensagem()
    else:
        print('As coordenadas do 1º ponto não podem ser maior que a do 2º ponto')
        return mensagem()

def maior_0(x1, x2, y1, y2):
    if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
        return area_retangulo(x1, x2, y1, y2)
    else:
        print('As coordenadas tem que ser mamior que 0')
        return mensagem()


main()
