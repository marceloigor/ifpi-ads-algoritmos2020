# 8. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

# Entrada 
binario = int(input('Digite um valor binario de 4 digitos: '))

# Processamento
digito4 = (binario // 1000) * 8
resto = binario % 1000

digito3 = (resto // 100) * 4
resto = resto % 100

digito2 = (resto // 10) * 2
digito1 = (resto % 10) * 1

decimal = digito1 + digito2 + digito3 + digito4

# Saída
print(f'binário {binario} = Decinal {decimal}')