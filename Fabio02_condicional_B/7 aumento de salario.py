"""
7. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
· o salário antes do reajuste;
· o percentual de aumento aplicado;
· o valor do aumento;
· o novo salário, após o aumento.
"""

def main():
    mensagem()

def mensagem():
    salario = float(input('Digite seu salário: R$ '))

    reajuste(salario)

def reajuste(salario):
    if salario >= 1500.00:
        porc = 5
    elif salario >= 700.00:
        porc = 10
    elif salario >= 280.00:
        porc = 15
    elif salario > 0:
        porc = 20
    else:
        print('Valor inválido!')
        return mensagem()
        
    aumento = calcular_porcento(salario, porc)
    novo_salario = salario + aumento
    print(f'\nValor do salário antes do reajuste:        R$ {salario:.2f}')
    print(f'Valor do percentual de aumento aplicado:   {porc} %')
    print(f'Valor do valor do aumento:                 R$ {aumento:.2f}')
    print(f'Valor do novo salário, após o aumento:     R$ {novo_salario:.2f}')

def calcular_porcento(salario, porc):
    porcentual = porc / 100 * salario
    return porcentual


main()