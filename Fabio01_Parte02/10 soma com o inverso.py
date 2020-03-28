# 10. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

# Entrada
valor = int(input('Digite um número de 3 dígitos: '))

# Processamento
digito1 = valor // 100
digito2 = (valor % 100) // 10
digito3 = (valor % 100) % 10

inverso = str(digito3) + str(digito2) + str(digito1)
soma = valor + int(inverso)

# Saída
print(f'{valor} + {inverso} = {soma}')
