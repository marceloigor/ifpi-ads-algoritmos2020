# 5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.

def main():
    mensagem()

def mensagem():
    produto_1 =  float(input('Digite o valor do 1º produto: '))
    produto_2 =  float(input('Digite o valor do 2º produto: '))
    produto_3 =  float(input('Digite o valor do 3º produto: '))

    mais_barato(produto_1, produto_2, produto_3)

def mais_barato(p1, p2, p3):
    if p1 < p2 and p1 < p3:
        print(f'{p1} é o mais barato.')
    
    if p2 < p1 and p2 < p3:
        print(f'{p2} é o mais barato.')

    if p3 < p1 and p3 < p2:
        print(f'{p3} é o mais barato.')

    if p1 == p2 or p1 == p3 or p2 == p3:
        print('Existe mais de 1 produto com o preço baixo.')


main()