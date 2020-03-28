# 10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

def main():
    mensagem()

def mensagem():
    dia, mes, ano = map(int, input('Digite uma data: ').split('/'))

    validar(dia, mes, ano)

def validar(dia, mes, ano):
    if (mes >= 1 and mes <= 12) and (ano >= 1920 and ano <= 2020):
        verificar_mes(mes, ano)
        if verificar_dia(dia, verificar_mes(mes, ano)) == True:
            print('Dia válido/ Data válida')
        else:
            print('Dia inválido/ Data inválida')
            return mensagem()
    else:
        print('Mês e ano inválido')
        return mensagem()

def ano_bissexto(ano):
    if (ano % 4) == 0:
        return True # É bissexto
    else:
        return False # Não é bissexto

def verificar_dia(dia, qtd_dia_mes):
    if dia >= 1 and dia <= qtd_dia_mes:
        return True
    else:
        return False

def verificar_mes(mes, ano):
    mes_e = 0
    if mes >= 1 and mes <= 7:
        if mes == 2:
            if ano_bissexto(ano) == True: # se é bissexto
                mes_e = 29
            else: # se não é bissexto
                mes_e = 28
        elif dias_mes(mes) == True: # se for par
            mes_e = 30
        else: # se for impar
            mes_e = 31
    else:
        if dias_mes(mes) == True: # se for par
            mes_e = 31
        else: # se for impar
            mes_e = 30
    return mes_e

def dias_mes(mes):
    if mes % 2 == 0:
        return True # É par = 30 dias
    else:
        return False # É impar = 31 dias


main()
