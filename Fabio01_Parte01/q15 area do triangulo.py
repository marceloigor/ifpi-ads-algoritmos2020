# 15. Leia o valor da base e altura de um triângulo, 
# calcule e escreva sua área. (área=(base * altura)/2)

# Entrada
base, altura = map(float, input('Digite a base e a altura do triângulo: ').split(','))

# Processamento
area = (base * altura) / 2

# Saída
print(f'A área do triângulo é igual à {area}')
