# 19. Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1
# (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo. (pdf)

# Entrada
x1, x2 = map(float, input('Digite o valor x1 e x2 do ponto 1: ').split(', '))
y1, y2 = map(float, input('Digite o valor y1 e y2 do ponto 2: ').split(', '))

# Processamento
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# Saída
print(f'A distância entre os pontos é {distancia:.2f}')