"""
27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
nascimento e a data (dia, mês e ano) atual.
"""

def main():
    mensagem()

def mensagem():
    dia_n, mes_n, ano_n = map(int, input('Digite sua data de nascimento: ').split('/'))
    dia_a, mes_a, ano_a = map(int, input('Digite a data atual: ').split('/'))

    idade_pessoa(dia_n, mes_n, ano_n, dia_a, mes_a, ano_a)

def idade_pessoa(dia_n, mes_n, ano_n, dia_a, mes_a, ano_a):
    data_atual = str(dia_a) + '/' + str(mes_a) + '/' + str(ano_a)
    data_nascimento = str(dia_n) + '/' + str(mes_n) + '/' + str(ano_n)

    anos = ano_a - ano_n

    if data_atual == data_nascimento:
        print (f'Datas iguais {data_atual}')

    elif mes_n > mes_a:
        anos -= 1
        meses = mes_n - mes_a

        if dia_n > dia_a:
            dias = dia_n - dia_a
        else:
            dias = dia_a - dia_n

    elif mes_n < mes_a:
        meses = mes_a - mes_n
        if dia_n > dia_a:
            dias = dia_n - dia_a #-31
        else:
            dias = dia_a - dia_n
    
    else:
        if dia_n > dia_a:
            anos -= 1
            meses = mes_n - mes_a
            dias = dia_n - dia_a
        else:
            meses = mes_a - mes_n
            dias = dia_a - dia_n
    
    print(anos, meses, dias)


main()
