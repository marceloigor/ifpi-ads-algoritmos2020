"""
19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
(IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).
"""

def main():
    altura = float(input('Digite a altura(m): '))
    peso = float(input('Digite o peso(kg): '))

    imc(altura, peso)

def imc(altura, peso):
    imc = peso // altura ** 2

    if imc < 25:
        print('A pessoa está com peso normal')
    elif imc >= 25 and imc < 30:
        print('A pessoa está obesa')
    else:
        print('A pessoa está com obesidade mórbida')


main()
