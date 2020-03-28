# 7. Leia um número inteiro de minutos, calcule e escreva 
# quantos dias, quantas horas e quantos minutos ele corresponde.

# Entrada
minutos = int(input('Digite um valor em minutos: '))

# Processamento
dia = minutos // 1440
resto = (minutos % 1440)
horas = resto // 60
minuto = resto % 60

# Saída
print(f'{minutos} minutos é equivalente à {dia} dia, {horas} hora e {minuto} minuto')