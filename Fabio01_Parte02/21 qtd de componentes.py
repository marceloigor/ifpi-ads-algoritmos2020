# 21. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que
# calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão
# (em kg), informada pelo usuário.

# Entrada
qtd_kg = float(input('Digite a quantidade de latão(em kg): '))

# Processamento
qtd_cobre = (qtd_kg / 100) * 70
qtd_zinco = (qtd_kg / 100) * 30

# Saída
print(f'{qtd_cobre} kg de cobre \n{qtd_zinco} kg de zinco')
