"""
9. Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), 
se digitar outro valor deve aparecer valor inválido.
"""

def main():
    mensagem()

def mensagem():
    numero = int(input('Digite um dia correspondente da semana: '))

    dia_semana(numero)

def dia_semana(numero):
    if numero == 1:
        print('Domingo')
    elif numero == 2:
        print('Segunda') 
    elif numero == 3:
        print('Terca Feira')
    elif numero == 4:
        print('Quarta Feira') 
    elif numero == 5:
        print('Quinta Feira')
    elif numero == 6:
        print('Sexta Feira') 
    elif numero == 7:
        print('Sábado') 
    else:
        print('Valor Inválido')
        return mensagem()


main()