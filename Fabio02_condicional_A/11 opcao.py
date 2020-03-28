"""
11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
possíveis para a variável opção são 1, 2 e 3.
"""

def main():
    mensage()

def validar_opcao(opcao, num1, num2, num3):
    if opcao >= 1 and opcao <=3:
        opcoes(opcao, num1, num2, num3)
    else:
        print('Opção inexistente')
        return mensage()

def opcoes(opcao, num1, num2, num3):
    if opcao == 1:
        print(num1)
    elif opcao == 2:
        print(num2)
    else:
        print(num3)

def mensage():
    opcao = int(input('Escolha um número entre(1, 2, 3): '))
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    num3 = int(input('Digite um número: '))

    validar_opcao(opcao, num1, num2, num3)


main()
