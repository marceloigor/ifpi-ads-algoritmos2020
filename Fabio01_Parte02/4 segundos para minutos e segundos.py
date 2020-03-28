# Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

# Entrada
segundos = int(input('Digite um valor em segundos: '))

# Processamento
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundo = segundos % 60

# Saída
print(f'{segundos} segundos é equivalente a {horas} horas {minutos} minutos e {segundo} segundos')
