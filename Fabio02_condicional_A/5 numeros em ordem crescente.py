# 5. Leia 3 (três) números e escreva-os em ordem crescente.

def main():

    valor_1 = int(input('Digite o 1º valor: '))
    valor_2 = int(input('Digite o 2º valor: '))
    valor_3 = int(input('Digite o 3º valor: '))

    ordem_crescente(valor_1, valor_2, valor_3)

def ordem_crescente(v1, v2, v3):
    ordem = ''
    if v1 >= v2 and v1 >= v3:
        ordem = str(v1)
        if v2 >= v3:
            ordem += ' ' + str(v2) + ' ' + str(v3)
        else:
            ordem += ' ' + str(v3) + ' ' + str(v2)
        
    elif v2 >= v1 and v2 >= v3:
        ordem = str(v2)
        if v1 >= v3:
            ordem += ' ' + str(v1) + ' ' + str(v3)
        else:
            ordem += ' ' + str(v3) + ' ' + str(v1)

    else:
        ordem = str(v3)
        if v1 >= v2:
            ordem += ' ' + str(v1) + ' ' + str(v2)
        else:
            ordem += ' ' + str(v2) + ' ' + str(v1)


    print(ordem)


main()
