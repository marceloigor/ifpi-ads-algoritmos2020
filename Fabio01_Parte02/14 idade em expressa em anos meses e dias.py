# 14. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

# Entrada
idade_dias = int(input('Digite sua idade emm dias: '))

# Processamento
anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30

# Saída
print(f'{anos} anos, {meses} meses e {dias} dias')
