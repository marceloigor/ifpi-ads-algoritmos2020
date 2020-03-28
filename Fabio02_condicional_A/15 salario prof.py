# 15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. 
# #Escreva na tela qual dos professores tem salário total maior.

def main():
    qtd_aula_p1 = float(input('Digite a qtd de horas aula do 1º profº: '))
    valor_hora_p1 = float(input('Digite o valor (R$) por horas aula do 1º profº: '))
    qtd_aula_p2 = float(input('Digite a qtd de horas aula do 2º profº: '))
    valor_hora_p2 = float(input('Digite o valor (R$) por horas aula do 2º profº: '))

    maior_salario(qtd_aula_p1, qtd_aula_p2, valor_hora_p1, valor_hora_p2)

def salario(qtd_aula, valor_aula):
    salario_prof = valor_aula * qtd_aula
    return salario_prof

def maior_salario(qtd_aula1, qtd_aula2, valor_aula1, valor_aula2):
    salario1 = salario(qtd_aula1, valor_aula1)
    salario2 = salario(qtd_aula2, valor_aula2)
    if salario1 > salario2:
        print(f'O sálario do 1º professor é maior. \nSalário = {salario1}')
    elif salario1 == salario2:
        print(f'Ambos professores tem o mesmo salário. \nSalário = {salario1}')
    else:
        print(f'O sálario do 2º professor é maior. \nSalário = {salario2}')






main()
