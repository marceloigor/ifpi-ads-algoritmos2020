# 16. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: (pdf)

# Entrada
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

# Processamento
r = (a + b) ** 2
s = (b + c) ** 2
d = (r + s) // 2

# Saída
print(f'D = {d}')
