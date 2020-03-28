# 6. Leia uma velocidade em km/h, calcule e escreva esta 
# velocidade em m/s. (Vm/s = Vkm/h / 3.6)

#Entrada
velocidade_kmh = int(input('Digite a velocidade em Km/h: '))

# Processamento
velocidade_ms = velocidade_kmh / 3.6

# Saída
print(f'{velocidade_kmh} km/h é equivalente a {velocidade_ms:.1f} m/s')