"""
20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
quarto) em que o ângulo se localiza.
"""

def main():
    mensagem()    

def quadrante(angulo):
    if angulo >= 0 and angulo <= 90:
        print('Primeiro quadrante')
    elif angulo > 90 and angulo <= 180:
        print('Segundo quadrante')
    elif angulo > 180 and angulo <= 270:
        print('Terceiro quadrante')
    else:
        print('Quarto quadrante')

def mensagem():
    angulo = int(input('Digite o ângulo: '))
    validar(angulo)

def validar(angulo):
    if angulo >= 0 and angulo <= 360:
        quadrante(angulo)
    else:
        mensagem()


main()
