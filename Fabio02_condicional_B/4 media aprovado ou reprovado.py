"""
4. Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez
"""

def main():
    mensagem()

def mensagem():
    nota_1 = float(input('Digite sua 1º nota: '))
    nota_2 = float(input('Digite sua 2º nota: '))

    media(nota_1, nota_2)

def media(n1, n2):
    media = (n1 + n2) / 2
    if media == 10.0:
        print(f'Aprovado com Distinção. \nMédia = {media}')
    elif media >= 7.0:
        print(f'Aprovado. \nMédia = {media}')
    else:
        print(f'Reprovado. \nMédia = {media}')


main()