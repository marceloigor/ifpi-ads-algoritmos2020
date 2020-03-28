# 8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva sua idade exata (em anos).

def main():
    mensagem()

def mensagem():
    print('Ex: 01/01/2020') 
    dia_atual, mes_atual, ano_atual = map(int, input('Digite a data atual: ').split('/'))
    dia_nasc, mes_nasc, ano_nasc = map(int, input('Digite a data de nascimento: ').split('/'))

    idade_exata_anos(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual)

def idade_exata_anos(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual):
    if mes_atual >= mes_nasc and ano_atual >= ano_nasc:
        anos = ano_atual - ano_nasc
    elif ano_atual < ano_nasc:
        print('A data de nascimento não pode ser maior que a data atual.')
        return mensagem()
    else:
        anos = (ano_atual - 1) - ano_nasc
        
    print(f'Sua idade exata é {anos} ano(s)')


main()

