# 12. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. 
# Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

# Entrada
valor = int(input('Digite um valor inteiro de 4 dígitos: '))

# Processamento
m = valor // 1000
resto = (valor % 1000)
c = resto // 100
resto = valor % 100
d = resto // 10
u = resto % 10

soma = m + c + d + u

# Saída
print(f'{m} + {c} + {d} + {u} = {soma}')
