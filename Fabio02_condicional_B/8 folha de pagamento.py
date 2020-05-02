"""
8. Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.
 Salário Bruto: (5 * 220) : R$ 1100,00
 (-) IR (5%) : R$ 55,00
 (-) INSS ( 10%) : R$ 110,00
 FGTS (11%) : R$ 121,00
 
 Total de descontos : R$ 165,00
 Salário Liquido : R$ 935,00
"""

def main():
    mensagem()

def mensagem():
    valor_hora = float(input('Digite o valor de sua hora: R$ '))
    qtd_hora = int(input('Digite o quantidade de horas trabalhadas: '))

    folha_pagamento(valor_hora, qtd_hora)

def folha_pagamento(valor_hora, qtd_hora):
    salario_bruto = valor_hora * qtd_hora
    ir = porcento(salario_bruto, 5)
    inss = porcento(salario_bruto, 10)
    fgts = porcento(salario_bruto, 11)
    descontos = ir + inss
    salario_liquido = salario_bruto - ir - inss

    mostrar = f'\nSalário Bruto :            R$ {salario_bruto:.2f} \
                \n(-) IR (5%) :              R$ {ir:.2f}\
                \n(-) INSS ( 10%) :          R$ {inss:.2f}\
                \nFGTS (11%) :               R$ {fgts:.2f}\
                \n\nTotal de descontos :       R$ {descontos:.2f}\
                \nSalário Liquido :          R$ {salario_liquido:.2f}'

    print(mostrar)

def porcento(salario_bruto, porc):
    porcen = porc / 100 * salario_bruto   
    return porcen

main()