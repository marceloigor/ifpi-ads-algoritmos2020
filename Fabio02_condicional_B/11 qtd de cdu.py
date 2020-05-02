"""
11. Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades
"""

def main():
    mensagem()

def mensagem():
    numero = int(input('Digite um valor menor que 1000: '))

    validar_numero(numero)

def validar_numero(numero):
    if numero > 0 and numero < 1000:
        qtd_cdu(numero)
    else:
        print('Valor Inválido')
        return mensagem()

def qtd_cdu(numero):
    mostar = ''
    c = numero // 100
    d = (numero % 100) // 10
    u = numero % 10
    if c == 1:
        mostar += str(c) + ' centena, '
    elif c == 0:
        mostar = ''
    else:
        mostar += str(c) + ' centenas, '    
    if c == 0 and d == 0:
        mostar = ''
    elif d == 1 or d == 0:
        mostar += str(d) + ' dezena e '
    else:
        mostar += str(d) + ' dezenas e '
    
    if u == 1 or u == 0:
        mostar += str(u) + ' unidade'
    else:
        mostar += str(u) + ' unidades'
    
    print(numero, '=', mostar)


main()