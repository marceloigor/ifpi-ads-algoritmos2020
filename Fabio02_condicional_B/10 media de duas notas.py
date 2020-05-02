"""
10. Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
sua média. A atribuição de conceitos obedece à tabela abaixo:
 Média de Aproveitamento Conceito
 Entre 9.0 e 10.0 A
 Entre 7.5 e 9.0 B
 Entre 6.0 e 7.5 C
 Entre 4.0 e 6.0 D
 Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

def main():
    mensagem()

def mensagem():
    nota_1 = float(input('Digite a 1º nota: '))
    nota_2 = float(input('Digite a 2º nota: '))

    conceito(nota_1, nota_2)

def conceito(n1, n2):
    media_aluno = n1 + n2 / 2
    print(f'Media = {media_aluno}')
    
    if n1 < 0 or n2 < 0:
        print('Nota não pode ser menor que 0.')
        return mensagem()

    if media_aluno > 9.0 and media_aluno >= 10.0:
        print('A \nAPROVADO')
    elif media_aluno > 7.5:
        print('B \nAPROVADO')
    elif media_aluno > 6.0:
        print('C \nAPROVADO')
    elif media_aluno > 4.0:
        print('D \nREPROVADO')  
    else:
        print('E \nREPROVADO') 


main()