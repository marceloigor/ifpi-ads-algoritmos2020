# 12. Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

# Entrada
salario = float(input('Digite o valor do salário: '))

# Processamento
aumento = (salario / 100) * 25
novo_salario = salario + aumento

# Saída
print(f'Seu novo salário é de R$ {novo_salario} reais.')
