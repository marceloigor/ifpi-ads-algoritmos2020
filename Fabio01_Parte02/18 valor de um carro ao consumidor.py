# 18. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do
# distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica
# de um carro e escreva o custo ao consumidor.

# Entrada
valor_carro = float(input('Digite o valor de fábrica do carro: '))

# Processamento
p_distribuidor = (valor_carro / 100) * 28
imposto = (valor_carro / 100) * 45

valor_final = valor_carro + p_distribuidor + imposto

# Saída
print(f'Valor final do carro é {valor_final}')
