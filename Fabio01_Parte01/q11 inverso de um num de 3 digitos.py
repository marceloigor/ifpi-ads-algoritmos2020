# 11. Leia um número inteiro (3 dígitos) e escreva o inverso 
# do número. (Ex.: número = 532 ; inverso = 235)

# Entrada
valor = int(input('Digite um valor de 3 dígitos: '))

# Processamento
c = valor // 100 
d = (valor % 100) // 10
u = valor % 10
inverso = str(u) + str(d) + str(c)

# Saída
print(f'Número = {valor} ; inverso = {inverso}')