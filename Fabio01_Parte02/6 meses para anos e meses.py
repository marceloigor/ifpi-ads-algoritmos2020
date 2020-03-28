# 6. Leia um número inteiro de meses, calcule e escreva 
# quantos anos e quantos meses ele corresponde

# Entrada
meses = int(input('Digite um valor em meses: '))

# Processamento 
anos = meses // 12
mes = meses % 12

# Saída
print(f'{meses} meses é equivalente a {anos} ano e {mes} mês')