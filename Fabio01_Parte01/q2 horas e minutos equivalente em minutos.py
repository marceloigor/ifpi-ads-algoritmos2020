# 2. Leia um valor em horas e um valor em minutos, 
# calcule e escreva o equivalente em minutos.

# Entrada
valor_horas = int(input('Digite um valor em horas: '))
valor_minutos = int(input('Digite um valor em minutos: '))

# Processamento
equivalente_minutos = valor_horas * 60 + valor_minutos

# Saída
print(f'{valor_horas}:{valor_minutos} h é equivalente a {equivalente_minutos} minutos.')
