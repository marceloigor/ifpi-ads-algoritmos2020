# 15. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

# Entrada
print('Ex.: 1/2')
numerador1, denominador1 =  map(int, input('Digite uma fração:').split('/'))
numerador2, denominador2 =  map(int, input('Digite uma 2º fração:').split('/'))

# Processamento
denominador = denominador1 * denominador2
numerador = ((denominador // denominador1) * numerador1) + ((denominador // denominador2) * numerador2)

# Saída
print(f'{numerador}/{denominador}')
