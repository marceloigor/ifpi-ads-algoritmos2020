"""
6. Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino 
ou N para Noturno e escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
ou "Valor Inválido!", conforme o caso.
"""

def main():
    mensagem()

def mensagem():
    turno = input('Digite o turno que você estuda: ')

    saudacao(turno)

def saudacao(turno):
    if turno == 'M' or turno == 'm':
        print('Bom dia!')
    elif turno == 'V' or turno == 'v':
        print('Boa tarde!')
    elif turno == 'N' or turno == 'n':
        print('Boa noite!')
    else:
        print('Valor inválido!')
        return mensagem()

main()