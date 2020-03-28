# 9. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso

# Entrada
valor = int(input('Digite um valor inteiro de 3 dígitos: '))

# Processamento
digito1 = valor // 100
digito2 = (valor % 100) // 10
digito3 = (valor % 100) % 10

inverso = str(digito3) + str(digito2) + str(digito1)
diferenca = valor - int(inverso)

# Saída
print(f'{valor} - {inverso} = {diferenca}')