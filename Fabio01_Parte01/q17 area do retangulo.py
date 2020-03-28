# 17. Leia o valor da base e altura de um retângulo, calcule e escreva sua área. (área = base * altura)

# Entrada
base, altura = map(float, input('Digite o valor da base e altura: ').split(','))

# Processamento
area = base * altura

# Saída
print(f'A área do retangulo = {area}')