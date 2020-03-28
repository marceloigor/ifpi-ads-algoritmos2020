# 8. Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

# Entrada
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

# Processamento
subtracao = valor1 - valor2
soma = valor1 + valor2
divisao = soma // subtracao

# Saída
print(f'A divisão da soma pela subtração dos números lidos é {divisao}')
