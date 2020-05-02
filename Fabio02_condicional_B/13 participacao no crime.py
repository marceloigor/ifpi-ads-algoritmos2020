"""
13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima ?"
b) "Esteve no local do crime ?"
c) "Mora perto da vítima ?"
d) "Devia para a vítima ?"
e) "Já trabalhou com a vítima ?"
O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

def main():
    mensagem()

def mensagem():
    input('Responda 5 perguntas sobre um crime: Digite 0 para NÃO ou 1 para SIM\nPressione ENTER para continuar... ')
    a = int(input('\na) Telefonou para a vítima?\n   0- NÃO   1- SIM\n Resposta: '))
    b = int(input('b) Esteve no local do crime?\n   0- NÃO   1- SIM\n Resposta: '))
    c = int(input('c) Mora perto da vítima?\n   0- NÃO   1- SIM\n Resposta: '))
    d = int(input('d) Devia para a vítima?\n   0- NÃO   1- SIM\n Resposta: '))
    e = int(input('e) Já trabalhou com a vítima?\n   0- NÃO   1- SIM\n Resposta: '))

    validar_respostas(a, b, c, d, e)

    
def classificacao(a, b, c, d, e):
    somatorio_questao = a + b + c + d + e
    if somatorio_questao > 4:
        print('Você é o Assassino')
    elif somatorio_questao > 2:
        print('Você é Cúmplice')
    elif somatorio_questao > 0:
        print('Você é Suspeito')
    else:
        print('Você é Inocente')


def validar_respostas(a, b, c, d, e):
    if a == 0 or a == 1:
        if b == 0 or b == 1:
            if c == 0 or c == 1:
                if d == 0 or d == 1:
                    if e == 0 or e == 1:
                        classificacao(a, b, c, d, e)
                    else:
                        print('Resposta Inválida')
                        return mensagem()
                else:
                    print('Resposta Inválida')
                    return mensagem()
            else:
                print('Resposta Inválida')
                return mensagem()
        else:
            print('Resposta Inválida')
            return mensagem()
    else:
        print('Resposta Inválida')
        return mensagem()


main()