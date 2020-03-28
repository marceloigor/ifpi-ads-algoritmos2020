"""
30. Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.
"""

def main():
    mensagem()
    
def mensagem():
    valor = int(input('Digite um número de 4 dígitos: '))

    validar_digito(valor)

def numero_original(valor):
    if validar_original(valor) == valor:
        print(f'{valor} é um número original.')
    else:
        print(f'{valor} não é um número original.')

def validar_original(valor):
    cm = valor // 100
    ud = valor % 100
    soma = cm + ud
    original = soma ** 2
    return original

def validar_digito(valor):
    if valor >= 1000 and valor <= 9999:
        numero_original(valor)
    else:
        print('Número inválido')
        mensagem()


main()
