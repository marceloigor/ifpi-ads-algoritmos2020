"""
29. Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.
Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.
"""

def main():
    mensagem()
    
def mensagem():
    valor = int(input('Digite um número de 4 dígitos: '))

    validar_digito(valor)

def quadrado_perfeito(valor):
    raiz_quadrada = valor ** 0.5
    soma = cent_mil(valor) + dez_uni(valor)
    print(raiz_quadrada, soma)

    if soma == raiz_quadrada:
        print(f'{valor} é um quadrado perfeito.')
        print(f'Pois √{valor} = {raiz_quadrada} = {cent_mil(valor)} + {dez_uni(valor)}')
    else:
        print(f'{valor} não é um quadrado perfeito.')
        print(f'Pois √{valor} = {raiz_quadrada} = {cent_mil(valor)} + {dez_uni(valor)}')

def validar_digito(valor):
    if valor >= 1000 and valor <= 9999:
        quadrado_perfeito(valor)
    else:
        print('Número inválido')
        mensagem()

def cent_mil(valor):
    cm = valor // 100
    return cm

def dez_uni(valor):
    du = valor % 100
    return du

main()
