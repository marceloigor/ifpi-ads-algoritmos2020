# 14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

def main():
    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))
    valor_3 = int(input('Digite o 3º valor: '))
    valor_4 = int(input('Digite o 4º valor: '))
    valor_5 = int(input('Digite o 5º valor: '))

    maior_media(valor_1, valor_2, valor_3, valor_4, valor_5)

def maior_media(v1, v2, v3, v4, v5):
    maior = ''
    media = media = (v1 + v2 + v3 + v4 + v5) // 5
    if v1 > media:
        maior += str(v1) + ' '
    if v2 > media:
        maior += str(v2) + ' '
    if v3 > media:
        maior += str(v3) + ' '
    if v4 > media:
        maior += str(v4) + ' '
    if v5 > media:
        maior += str(v5)
    if maior == '':
        maior = 'Nenhum valor'
    print(f'média = {media} \n{maior} é maior que a média.')


main()
