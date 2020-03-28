# Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

# Entrada
dias = int(input('Digite um valor em dias: '))

# Processamento
semanas = dias // 7
dia = dias % 7

# Saída
print(f'{dias} dias é equivalente a {semanas} semanas e {dia} dias')
