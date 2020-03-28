"""
16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
escreva “Reprovado”.
"""

def main():
    nota_1 = float(input('Digite a 1º nota: '))
    nota_2 = float(input('Digite a 2º nota: '))

    situacao(nota_1, nota_2)

def media(n1, n2):
    media_aluno = (n1 + n2) / 2
    return media_aluno

def situacao(nota_1, nota_2):
    media_principal = media(nota_1, nota_2)
    if media_principal >= 7.0:
        print('Aprovado')
    else:
        exame_final = float(input('Digite a nota do exame final: '))
        media_final = media(media_principal, exame_final)
        if media_final >= 5.0:
            print('Aprovado por exame final.')
        else:
            print('Reprovado')


main()
