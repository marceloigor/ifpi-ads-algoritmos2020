# 19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)

# Entrada
raio = float(input('Digite o valor do raio de uma esfera: '))

# Processamento
volume = (4 * 3.14) * (raio ** 3)

# Saída 
print(f'O volume da esfera = {volume}')