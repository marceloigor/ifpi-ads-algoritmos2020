# 7. Leia 3 números, calcule e escreva a soma dos 2 primeiros 
# e a diferença entre os 2 últimos.

# Entrada
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

# Processamento
soma = num1 + num2
diferenca = num2 - num3

print(f'Soma {num1} + {num2} = {soma} \nDiferença {num2} - {num3} = {diferenca}')