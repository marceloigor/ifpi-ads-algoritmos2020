# 3. Leia um valor em minutos, calcule e escreva o equivalente 
# em horas e minutos.

# Entrada
valor_min = int(input('Digite um valor em minutos: '))

# Processamento
equivalente_horas = valor_min // 60
equivalente_min = valor_min % 60

# Saída
print(f'{valor_min} minutos é equivalente a {equivalente_horas}:{equivalente_min} h')