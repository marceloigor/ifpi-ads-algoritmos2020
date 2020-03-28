"""
24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas 
raízes. Vale lembrar que o coeficiente A deve ser diferente de 0 (zero).
"""

def main():
    mensagem()
    
def mensagem():
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))

    equacao(a, b, c)

def equacao(a, b, c):
    if a != 0:
        raizes(a, b, c) 
    else:
        print('o valor de "A" tem que ser diferente de 0')
        return mensagem()

def raizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + (delta ** 0.5)) // (2 * a)
    x2 = (-b - (delta ** 0.5)) // (2 * a)

    equacao1 = (a * x1) ** 2 + b * x1 + c
    equacao2 = (a * x2) ** 2 + b * x2 + c
    if equacao1 == 0 and equacao2 == 0:
        print('Equação de 2º gral')
    else:
        print('nao é')



main()
