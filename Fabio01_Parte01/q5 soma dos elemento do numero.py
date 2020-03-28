# 5. Leia um número inteiro (3 dígitos), calcule e escreva a 
# soma de seus elementos (C + D + U).

# Entrada
valor = int(input('Digite um valor de 3 dígitos: '))

# Processamento
c = valor // 100
d = (valor % 100) // 10
u = (valor % 10)
somatorio = c + d + u

# Saída
print(f'A soma dos elementos do número {valor} é igual à {somatorio}')