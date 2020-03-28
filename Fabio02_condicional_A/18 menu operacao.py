"""
18. Leia dois valores e uma das seguintes operações a serem executadas
(codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão).
Calcule e escreva o resultado dessa operação sobre os dois valores lidos.
"""

def main():

    valor_1 = int(input('Digite 1º valor: '))
    valor_2 = int(input('Digite 2º valor: '))
    mensage(valor_1, valor_2)

def mensage(valor_1, valor_2):
    mensagem = '\nDeseja executar qual das seguintes operações? \
                \n1 – Adição \n2 – Subtração \n3 – Multiplicação \n4 – Divisão \nOpção --> '

    operacao = int(input(mensagem))

    validar_operacao(operacao, valor_1, valor_2)

def validar_operacao(operacao, v1, v2):
    if operacao == 1:
        adicao(v1, v2)
    elif operacao == 2:
        subtracao(v1, v2)
    elif operacao == 3:
        multiplicacao(v1, v2)
    elif operacao == 4:
        divisao(v1, v2)
    else:
        return mensage(v1, v2)
        

def adicao(v1, v2):
    soma = v1 + v2
    print(f'A adição de {v1} + {v2} = {soma}')

def subtracao(v1, v2):
    subtrair = v1 - v2
    print(f'A subtração de {v1} - {v2} = {subtrair}')

def multiplicacao(v1, v2):
    multiplicar = v1 * v2
    print(f'A multiplicação de {v1} * {v2} = {multiplicar}')

def divisao(v1, v2):
    dividir = v1 // v2
    print(f'A divisão de {v1} / {v2} = {dividir}')


main()
