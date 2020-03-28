"""
23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
recente
"""

def main():
    dia, mes, ano = map(int, input('digite a 1º data: ').split('/'))
    dia2, mes2, ano2 = map(int, input('digite a 2º data: ').split('/'))

    data_recente(dia, dia2, mes, mes2, ano, ano2)

def data_recente(d1, d2, m1, m2, a1, a2):
    if a2 > a1:
        print(f'{d2}/{m2}/{a2}')
    elif a1 > a2:
        print(f'{d1}/{m1}/{a1}')
    else:
        if m2 > m1:
            print(f'{d2}/{m2}/{a2}')
        elif m1 > m2:
            print(f'{d1}/{m1}/{a1}')
        else:
            if d2 > d1:
                print(f'{d2}/{m2}/{a2}')
            elif d1 > d2:
                print(f'{d1}/{m1}/{a1}')
            else:
                print('As datas são iguais.')


main()
