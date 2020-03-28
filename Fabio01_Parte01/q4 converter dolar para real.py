# 4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

# Entrada
valor_atual_dolar = float(input('digite o valor atual do dolar ($): '))
valor_dolar_converter = float(input('Digite o valor em dolar ($) para converter em real (R$): '))

# Processamento
valor_real = valor_dolar_converter * valor_atual_dolar

# Saída
print(f'$ {valor_dolar_converter} dolar é equivalente à R$ {valor_real} reais')
