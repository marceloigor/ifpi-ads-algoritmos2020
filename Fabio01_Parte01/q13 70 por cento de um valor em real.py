# 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

# Entrada
valor_real = float(input('Digite um valor em real (R$): '))

# Processamento
por_cento = (valor_real / 100) * 70

# Saída
print(f'70% de {valor_real:.2f} reais = {por_cento:.2f} reais')
